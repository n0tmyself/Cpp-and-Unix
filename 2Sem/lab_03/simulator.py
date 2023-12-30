from City_transport import *
from vehicleGenerator import VehicleGenerators
from copy import deepcopy
import random
from collections import deque
# from load import Load
import numpy as np


# defining the Simulator class
class Simulator:
    def __init__(self, config={}):
        # Setting default configuration
        self.set_default_config()
        self.n = [0] * 36
        self.num = [0] * 36

        # Updating configuration
        for attr, val in config.items():
            setattr(self, attr, val)

    def set_default_config(self):
        # Time keeping
        self.t = 840.0
        self.timeInterval = 10
        # Frame count keeping
        self.frame_count = 0
        # Simulation time step
        self.dt = 0.02
        # Array to store roads
        self.roads = {}
        self.vehicleGens = deque()
        self.trafficSignals = deque()
        self.loads = {}
        self.optimizer = True

    def createLoads(self):
        for road_key, road in self.roads.items():
            self.loads[road_key] = Load(road)

    def createRoad(self, start, end, startCross, endCross):
        the_road = Road(start, end, startCross, endCross)
        self.roads[(startCross, endCross)] = the_road
        return the_road

    def createTrafficSignal(self, trafficSignal):
        self.trafficSignals.append(trafficSignal)

    def createRoads(self, roadList):
        for the_road in roadList:
            self.createRoad(*the_road)

    def createRoadsFromGraph(self, Graph):
        self.graph = Graph
        offset = 1.1
        for i in range(len(Graph)):
            start = Graph[i][0]
            if len(Graph[i][1]) > 0:
                for j in Graph[i][1]:
                    end = Graph[j][0]
                    startCross = i
                    endCross = j
                    length = distance.euclidean(start, end)
                    sin = (end[1] - start[1]) / length
                    cos = (end[0] - start[0]) / length
                    self.createRoad((start[0] - offset * sin, start[1] + offset * cos),
                                    (end[0] - offset * sin, end[1] + offset * cos), startCross, endCross)

    def createGen(self, config):
        self.vehicleGens.append(VehicleGenerators(self, config))

    def update(self):
        # Updating every road
        for roadKey, road in self.roads.items():
            if len(road.vehicles) > 0 and road.vehicles[0].currentRoadIndex + 1 < len(road.vehicles[0].path):
                vehicle = road.vehicles[0]
                nextRoad = self.roads[vehicle.path[vehicle.currentRoadIndex + 1]]
            else:
                road.update(self.dt)
                nextRoad = None
            road.update(self.dt, nextRoad)

        for road_key, load in self.loads.items():
            load.update(self.dt, self.t)

        i = 0
        for roadKey, road in self.roads.items():
            self.n[i] = max(self.n[i], len(road.vehicles))
            i += 1

        if self.t % self.timeInterval == 0:
            # print(self.t, self.t % 15)
            # print(self.n)
            self.num = self.n
            self.n = [0] * 36

        k = 0
        # print(k)
        # Checking the roads for out of bounds vehicle
        for road_key, road in self.roads.items():
            # If road does not have vehicles, then continue
            if len(road.vehicles) == 0: continue
            # If not
            vehicle = road.vehicles[0]
            if vehicle.x >= road.length:
                if len(vehicle.path) == 1:
                    vehicle.currentRoadIndex = 1
                    newVehicle = deepcopy(vehicle)
                    newVehicle.x = 0
                    crossRoad = self.graph[road.endCross]
                    if len(crossRoad[1]) > 1:
                        if newVehicle.decideToRide():
                            # carNums = [len(self.roads[(road.endCross, k)].vehicles) for k in crossRoad[1]]
                            carNums = [self.num[j] for j in crossRoad[1]]
                            minNum = min(carNums)
                            minIdx = [i for i, x in enumerate(carNums) if x == minNum]
                            if not(self.optimizer):
                                nextCross = crossRoad[1][random.choice(minIdx)]
                            else:
                                nextCross = crossRoad[1][random.choice([i for i in range(len(crossRoad[1]))])]
                            k += 1
                            self.roads[(road.endCross, nextCross)].vehicles.append(newVehicle)
                        else:
                            pass

                # If vehicle has a next road
                if vehicle.currentRoadIndex + 1 < len(vehicle.path):
                    # Updating the current road to next road
                    vehicle.currentRoadIndex += 1
                    # Creating a copy and reseting some vehicle properties
                    newVehicle = deepcopy(vehicle)
                    newVehicle.x = 0
                    # Adding it to the next road
                    nextRoadIndex = vehicle.path[vehicle.currentRoadIndex]
                    self.roads[nextRoadIndex].vehicles.append(newVehicle)
                    # In all cases, removing it from its road
                road.vehicles.popleft()

        for signal in self.trafficSignals:
            signal.update(self)

        for gen in self.vehicleGens:
            gen.update()
            if (self.t >= 870 and self.t <= 990) or (self.t >= 1020 and self.t <= 1080):
                gen.vehicleRate = 40
            else:
                gen.vehicleRate = 30
        self.t = round(self.dt + self.t, 2)

        if self.t >= 1440:
            self.t = 0

from City_transport import *
from collections import deque

class Road:
    def __init__(self, start, end, startCross, endCross):
        self.start = start
        self.end = end
        self.startCross = startCross
        self.endCross = endCross
        self.initProperties()

    def initProperties(self):
        self.length = distance.euclidean(self.start, self.end)
        self.angleSin = (self.end[1] - self.start[1]) / self.length
        self.angleCos = (self.end[0] - self.start[0]) / self.length
        self.vehicles = deque()
        self.hasTrafficSignal = False

    def setTrafficSignal(self, signal, group):
        self.trafficSignal = signal
        self.trafficSignalGroup = group
        self.hasTrafficSignal = True

    @property
    def trafficSignalState(self):
        if self.hasTrafficSignal:
            i = self.trafficSignalGroup
            return self.trafficSignal.currentCycle[i]
        return True

    def update(self, dt, nextRoad=None, nextRoadAmount=30):
        num = len(self.vehicles)

        if num > 0:
            # Updating the first vehicle
            self.vehicles[0].update(None, dt)
            # Updating the other vehicles
            for i in range(1, num):
                lead = self.vehicles[i - 1]
                self.vehicles[i].update(lead, dt)

            # Checking for traffic signal
            if self.trafficSignalState:
                if nextRoad is not None:
                    if len(nextRoad.vehicles) >= nextRoadAmount and self.vehicles[0].x >= self.length - self.trafficSignal.stopDistance * 0.6:
                        self.vehicles[0].v = 0
                        self.vehicles[0].stopVehicle()
                    else:
                        self.vehicles[0].unstopVehicle()
                        for the_vehicle in self.vehicles:
                            the_vehicle.fastVehicle()
                else:
                    self.vehicles[0].unstopVehicle()
                    for the_vehicle in self.vehicles:
                        the_vehicle.fastVehicle()
            else:
                # In case the traffic signal is red
                if self.vehicles[0].x >= self.length - self.trafficSignal.slowDistance:
                    # Slowing vehicles down in slowing zone
                    self.vehicles[0].slowVehicle(self.trafficSignal.slowSpeed)
                if self.length - self.trafficSignal.stopDistance <= \
                        self.vehicles[0].x <= self.length - self.trafficSignal.stopDistance / 5:
                    # Stopping vehicles in the stop zone
                    self.vehicles[0].stopVehicle()

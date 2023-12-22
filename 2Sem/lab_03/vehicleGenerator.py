from numpy.random import randint
from City_transport import *
from Vehicles import Vehicle

class VehicleGenerators:
    def __init__(self, sim, config={}):
        self.set_default_config()
        self.simulation = sim
        self.lastAddedTime = self.simulation.t
        for attr, val in config.items():
            setattr(self, attr, val)

        self.initProperties()

    def set_default_config(self):
        self.vehicleRate = 20
        self.vehicles = [(1, {})]

    def initProperties(self):
        self.upcomingVehicle = self.generateVehicle()

    def generateVehicle(self):
        total = sum(pair[0] for pair in self.vehicles)
        n = randint(1, total + 1)
        for (weight, config) in self.vehicles:
            n -= weight
            if n <= 0:
                return Vehicle(config)

    def update(self):
        if self.simulation.t - self.lastAddedTime >= 60 / self.vehicleRate:
            road = self.simulation.roads[self.upcomingVehicle.path[0]]
            if len(road.vehicles) == 0 or road.vehicles[-1].x > self.upcomingVehicle.s_0 + self.upcomingVehicle.l:
                self.upcomingVehicle.timeAdded = self.simulation.t
                road.vehicles.append(self.upcomingVehicle)
                self.lastAddedTime = self.simulation.t
            self.upcomingVehicle = self.generateVehicle()
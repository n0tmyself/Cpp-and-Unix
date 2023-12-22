from City_transport import *

class Load:
    def __init__(self, road):
        self.road = road
        self.vehiclesNum = len(road.vehicles)
        self.startTime = None
        self.duration = 0
        if len(self.road.vehicles) > 0:
            self.roadCapacity = self.vehiclesNum * (self.road.vehicles[0].l + self.road.vehicles[0].s_0) / self.road.length * 100
        else:
            self.roadCapacity = 0


    def getLoad(self):
        return self.roadCapacity

    def getDurationOver90(self, currentTime):
        if self.startTime is not None:  # If capacity is currently over 90
            return self.duration + (currentTime - self.startTime)
        else:
            return self.duration

    def update(self, dt, currentTime):
        self.road.update(dt)
        self.vehiclesNum = len(self.road.vehicles)
        self.oldCapacity = self.roadCapacity
        if len(self.road.vehicles) > 0:
            self.roadCapacity = self.vehiclesNum * (self.road.vehicles[0].l + self.road.vehicles[0].s_0) / self.road.length * 100
        else:
            self.roadCapacity = 0

        if self.roadCapacity >= 90 and self.oldCapacity < 90:  # Capacity just crossed 90
            self.startTime = currentTime
        elif self.roadCapacity < 90 and self.oldCapacity >= 90:  # Capacity just dropped below 90
            if self.startTime is not None:
                self.duration = currentTime - self.startTime
                self.startTime = None
        elif self.roadCapacity < 90:
            self.duration = 0





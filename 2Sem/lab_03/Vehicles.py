from City_transport import *
import numpy as np
import random


class Vehicle:
    def __init__(self, config={}):
        self.set_default_config()

        for attr, val in config.items():
            setattr(self, attr, val)

        self.initProperties()


    def set_default_config(self):
        self.l = 2
        self.s_0 = 2
        self.T = 1
        self.vMax = 16.6
        self.aMax = 10**3
        self.bMax = 4.61

        self.path = []
        self.currentRoadIndex = 0
        self.moodToRide = 105

        self.x = 0
        self.v = self.vMax
        self.a = 0
        self.stopped = False


    def initProperties(self):
        self.sqrt_ab = 2 * np.sqrt(self.aMax * self.bMax)
        self._vMax = self.vMax

    def update(self, leadVehicle, dt):
        if self.v + self.a * dt < 0:
            self.x -= 1 / 2 * self.v * self.v / self.a
            self.v = 0
        else:
            self.v += self.a * dt
            self.x += self.v * dt + self.a * dt * dt / 2

        alpha = 0
        if leadVehicle:
            del_x = leadVehicle.x - self.x - leadVehicle.l
            del_v = self.v - leadVehicle.v

            alpha = (self.s_0 + max(0, self.T * self.v + del_v * self.v / self.sqrt_ab)) / del_x

        self.a = self.aMax * (1 - (self.v / self.vMax) ** 4 - alpha ** 2)

        if self.stopped:
            self.a = - self.bMax * self.v / self.vMax

        if self.v > self.vMax:
            self.v = self.vMax

    def decideToRide(self):
        self.moodToRide -= 5
        if self.moodToRide < 0:
            self.moodToRide = 0
        return random.randrange(1) < self.moodToRide

    def stopVehicle(self):
        self.stopped = True

    def unstopVehicle(self):
        self.stopped = False

    def slowVehicle(self, v):
        self.vMax = v

    def fastVehicle(self):
        self.vMax = self._vMax
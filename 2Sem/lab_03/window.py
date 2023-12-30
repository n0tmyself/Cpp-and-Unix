import pygame
from pygame import gfxdraw
import numpy as np
from datetime import time

import simulator


class Window:
    def __init__(self, simulator, config={}):
        # Simulation to draw
        self.simulator = simulator

        # Setting the default configurations
        self.set_default_config()

        # Updating the configurations
        for attr, val in config.items():
            setattr(self, attr, val)

    def set_default_config(self):
        """Setting the default configuration"""
        self.the_width = 1350
        self.the_height = 600
        self.the_bgColor = (250, 250, 250)

        self.the_fps = 144
        self.the_zoom = 5
        self.the_offset = (0, 0)

        self.mouseLast = (0, 0)
        self.mouseDown = False

    def loop(self, loop=None):
        """Showing a window visualizing the simulation and runs the loop function."""
        # Creating a pygame window
        self.screen = pygame.display.set_mode((self.the_width, self.the_height))
        pygame.display.flip()

        # Fixed fps
        clock = pygame.time.Clock()

        # To draw text
        pygame.font.init()
        self.text_font = pygame.font.SysFont('Lucida Console', 16)

        # Drawing loop
        running = True
        while running:
            # Updating the simulation
            if loop: loop(self.simulator)

            self.simulator.update()

            # Drawing simulation
            self.draw()

            # Updating the window
            pygame.display.update()
            clock.tick(self.the_fps)

            # Handling all events
            for event in pygame.event.get():
                # Handling mouse drag and wheel events
                if event.type == pygame.QUIT:
                    running = False

    def convert(self, x, y=None):
        """Converting the simulation coordinates to screen coordinates"""
        width, height = pygame.display.get_surface().get_size()
        max_x = width / 4
        max_y = height / 4
        screen_x = width * x / max_x
        screen_y = height * y / max_y
        return screen_x, screen_y

    def the_background(self, r, g, b):
        """Filling the screen with one color."""
        self.screen.fill(self.the_bgColor)

    def the_text(self, text, screen_x, screen_y, text_color=None):
        """Drawing a text"""
        if text_color == None:
            text_surface = self.text_font.render(text, True, (0, 0, 0))
            self.screen.blit(text_surface, (screen_x, screen_y))
        else:
            text_surface = self.text_font.render(text, True, text_color)
            self.screen.blit(text_surface, (screen_x, screen_y))

    def the_line(self, start_pos, end_pos, color, width=8):
        """Drawing a line."""
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)

    def the_rect(self, x1, y1, width, height, color=(255, 0, 0)):
        """Drawing a rectangle."""
        pygame.draw.rect(self.screen, color, pygame.Rect(x1, y1, width, height))

    def the_box(self, pos, size, color):
        """Drawing a rectangle."""
        ...

    def the_circle(self, pos, radius=3, color=(255, 0, 0), filled=True):
        """Drawing a circle"""
        pygame.draw.circle(self.screen, color, pos, radius)

    def the_polygon(self, vertices, color, filled=True):
        """Drawing a polygon"""

    def the_rotated_box(self, pos, size, angle=None, cos=None, sin=None, centered=True, color=(0, 0, 255), filled=True):
        """Drawing a filled rectangle centered at *pos* with size *size* rotated anti-clockwise by *angle*."""

    def the_rotated_rect(self, pos, size, angle=None, cos=None, sin=None, centered=True, color=(0, 0, 255)):
        """Drawing a rectangle centered at *pos* with size *size* rotated anti-clockwise by *angle*."""
        pygame.draw.rect(self.screen, color, pygame.Rect(*pos, *size))

    def drawAxes(self, color=(100, 100, 100)):
        """Drawing x and y axis"""

    def drawGrid(self, unit=50, color=(150, 150, 150)):
        """Drawing a grid"""

    def drawRoads(self, color=(128, 128, 128)):
        """Drawing every road"""
        for road_key, road in self.simulator.roads.items():
            start = self.convert(*road.start)
            end = self.convert(*road.end)
            self.the_line(start, end, color)

    def drawCrossroads(self):
        """Drawing numbers of crossroads"""
        crossroads = set()
        for road_key, road in self.simulator.roads.items():
            num = road.startCross
            if num not in crossroads:
                x, y = road.start
                screen_x, screen_y = self.convert(x, y)
                self.the_text(f'{num}', screen_x, screen_y)
            crossroads.add(num)


    def drawTrafficLigths(self):
        """Drawing traffic lights"""
        trafficOffset = 2
        red = (200, 0, 0)
        green = (0, 200, 0)
        for roadkey in self.simulator.roads:
            road = self.simulator.roads[roadkey]
            if road.hasTrafficSignal:
                x1, y1 = road.end
                x1 -= trafficOffset * road.angleCos
                y1 -= trafficOffset * road.angleSin
                x1, y1 = self.convert(x1, y1)
                # x1 -= 1 * road.angleSin
                x2 = x1 + 4 * road.angleSin
                # y1 -= 1 * road.angleCos
                y2 = y1 + 4 * road.angleCos
                if road.trafficSignalState:
                    self.the_line((x1, y1), (x2, y2), green, 8)
                else:
                    self.the_line((x1, y1), (x2, y2), red, 8)

    def drawTime(self):
        """drawing time"""
        hours = int(self.simulator.t // 60)
        minutes = int(self.simulator.t % 60)
        my_time = time(hours, minutes)
        time_int = time(0, self.simulator.timeInterval)
        self.the_text(f'current time: {my_time.strftime("%H:%M")}', 20, 20)
        self.the_text(f'Update interval: {time_int.strftime("%H:%M")}', 220, 20)

    def drawVehicles(self):
        for road_key, road in self.simulator.roads.items():
            if len(road.vehicles) >= 1:
                for car in road.vehicles:
                    positionX, positionY = road.start
                    positionX += car.x * road.angleCos
                    positionY += car.x * road.angleSin
                    position = self.convert(positionX, positionY)
                    self.the_circle(position)


    def drawLoad(self, x, y, trafficCycle=10, high_load=90):
        y_i = y
        red_text = (200, 0, 0)
        yellow_text = (210, 210, 0)
        green_text = (0, 150, 0)
        self.the_text('Highest traffic:', x, y_i)
        y_i += 20
        load_top = []
        i = 0
        for key, road in self.simulator.roads.items():
            # load = round(self.simulator.loads[key].getLoad())
            load = round(self.simulator.num[i] * 4 / road.length * 100)
            num_of_vehicles = self.simulator.num[i]
            i += 1
            if load > 0:
                if load <= high_load:
                    load_top.append([load, f'{road.startCross, road.endCross}: {num_of_vehicles}, {load} %', green_text])
                    # self.the_text(
                    #     f'{road.startCross, road.endCross}: {num_of_vehicles}, {load} %', x, y_i, green_text)
                elif 50 < load < 90:
                    load_top.append([load, f'{road.startCross, road.endCross}: {num_of_vehicles}, {load} %', yellow_text])
                    # self.the_text(
                    #     f'{road.startCross, road.endCross}: {num_of_vehicles}, {load} %', x, y_i, yellow_text)
                else:
                    if load > 100:
                        load_top.append([load, f'{road.startCross, road.endCross}: {num_of_vehicles}, 100 %', red_text])
                        # self.the_text(
                        #     f'{road.startCross, road.endCross}: {num_of_vehicles}, 100 %', x, y_i, red_text)
                    else:
                        load_top.append([load, f'{road.startCross, road.endCross}: {num_of_vehicles}, {load} %', red_text])
                        # self.the_text(
                        #     f'{road.startCross, road.endCross}: {num_of_vehicles}, {load} %', x, y_i, red_text)


                # if road.hasTrafficSignal and load >= high_load:
                #     car = road.vehicles[-1]
                #     if not road.trafficSignalState:
                #         additionalTime = trafficCycle - (self.simulator.t % trafficCycle)
                #     else:
                #         additionalTime = 0
                #     timeToDissolve = round((road.length - car.x) / car.vMax + additionalTime, 1)
                #     load_top[-1][1] += '; dissolving in: ' + str(timeToDissolve)
                #
                #     if load >= 90:
                #         duration = round(self.simulator.loads[key].getDurationOver90(self.simulator.t), 1)
                #         load_top[-1][1] += '; duration: ' + str(duration)


        load_top.sort(key=lambda x: x[0], reverse=True)
        if len(load_top) >= 0:
            for i in range(min(len(load_top), 10)):
                self.the_text(f'{i + 1}. {load_top[i][1]}', x, y_i, load_top[i][-1])
                y_i += 20

    def drawStatus(self):
        """Drawing status text"""
        self.drawTime()
        self.drawLoad(20, 60)



    def draw(self):
        # Filling the background
        self.the_background(*self.the_bgColor)

        # Major and minor grid and axes
        self.drawGrid(10, (220, 220, 220))
        self.drawGrid(100, (200, 200, 200))
        self.drawAxes()

        # Drawing roads
        self.drawRoads()
        self.drawVehicles()
        # Drawing the status info
        # self.drawStatus()
        # Drawing traffic signals
        self.drawTrafficLigths()
        self.drawCrossroads()
        self.drawStatus()
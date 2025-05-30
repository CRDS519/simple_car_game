import pygame
import math
from utils import *

class Sensor:
    def __init__(self, car, count, spread, length):
        self.car = car
        self.count = count
        self.spread = spread
        self.length = length

    def draw_sensor(self, screen, camera_y):
        debut_angle = self.spread/2
        angle_split = self.spread/(self.count - 1)
        for i in range(self.count):
            angle = debut_angle - i*angle_split + self.car.angle
            pygame.draw.line(screen, 'yellow', (self.car.x, self.car.y - camera_y), (self.car.x - self.length*math.sin(angle), self.car.y - camera_y - self.length*math.cos(angle)), 5)

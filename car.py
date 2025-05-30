import pygame
import math
from utils import *
from sensor import Sensor

class Car:
    def __init__(self, pos, width, length, color, control_type, max_speed):
        (self.x, self.y) = pos
        self.width = width
        self.length = length
        self.color = color
        self.control_type = control_type # user/dummy/ai
        self.max_speed = max_speed

        self.controls = {"forward" : False, "reverse" : False, "left" : False, "right": False}
        if self.control_type == "dummy":
            self.controls["forward"] = True

        if self.control_type != "dummy":
            self.sensors = Sensor(self, 5, math.pi/2, 200)

        self.speed = 0
        self.acceleration = 36
        self.friction = 1.2

        self.angle = 0
        self.angular_acc = 0.05

        self.poly = self.create_polygon()

        self.damaged = False

    def update(self, dt, borders = [], traffic = []):
        if self.damaged == False and self.control_type != "dummy":
            self.move(dt)
            self.assess_damage(borders, traffic)

        if self.control_type == "dummy":
            self.move(dt)

    def move(self, dt):
        if abs(self.speed) > 0:
            self.speed -= self.friction*self.speed*dt

        if self.controls["forward"]:
            self.speed = min(self.speed + self.acceleration*dt, self.max_speed)
        elif self.controls["reverse"]:
            self.speed = max(self.speed - self.acceleration*dt, -self.max_speed/2)

        if self.controls["left"]:
            self.angle += self.angular_acc*self.speed*dt
        elif self.controls["right"]:
            self.angle -= self.angular_acc*self.speed*dt

        if abs(self.speed) < self.friction/10:
            self.speed = 0

        self.x -= self.speed*math.sin(self.angle)
        self.y -= self.speed*math.cos(self.angle)

        self.poly = self.create_polygon()

    def assess_damage(self, borders, traffic):
        for border in borders:
            if poly_intersect(border, self.poly):
                self.damaged = True
                self.color = (82,82,82)
        
        for poly in traffic:
            if poly_intersect(poly, self.poly):
                self.damaged = True
                self.color = (82,82,82)

    def create_polygon(self):
        points = []
        dist = math.sqrt((self.length/2)**2 + (self.width/2)**2)
        alpha = math.atan(self.width/self.length)
        points.append(
            (self.x - dist*math.sin(alpha + self.angle), self.y - dist*math.cos(alpha + self.angle))
        )
        points.append(
            (self.x - dist*math.sin(-alpha + self.angle), self.y - dist*math.cos(-alpha + self.angle))
        )
        points.append(
            (self.x - dist*math.sin(math.pi + alpha + self.angle), self.y - dist*math.cos(math.pi + alpha + self.angle))
        )
        points.append(
            (self.x - dist*math.sin(math.pi - alpha + self.angle), self.y - dist*math.cos(math.pi - alpha + self.angle))
        )
        return points

    def draw(self, screen, camera_y):
        shifted = [(x, y - camera_y) for x, y in self.poly]
        pygame.draw.polygon(screen, self.color, shifted)

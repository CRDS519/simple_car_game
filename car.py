import pygame
import math

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

        self.speed = 0
        self.acceleration = 0.3
        self.friction = 0.02

        self.angle = 0
        self.angular_acc = 0.007

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        dt_multiplier = dt*60

        if abs(self.speed) > 0:
            self.speed -= self.friction*self.speed*dt_multiplier

        if self.controls["forward"]:
            self.speed = min(self.speed + self.acceleration*dt_multiplier, self.max_speed)
        elif self.controls["reverse"]:
            self.speed = max(self.speed - self.acceleration*dt_multiplier, -self.max_speed/2)

        if self.controls["left"]:
            self.angle += self.angular_acc*self.speed*dt_multiplier
        elif self.controls["right"]:
            self.angle -= self.angular_acc*self.speed*dt_multiplier

        if abs(self.speed) < self.friction:
            self.speed = 0

        self.x -= self.speed*math.sin(self.angle)
        self.y -= self.speed*math.cos(self.angle)

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
        poly = self.create_polygon()
        shifted = [(x, y - camera_y) for x, y in poly]
        pygame.draw.polygon(screen, self.color, shifted)

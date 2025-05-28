import pygame
import math

class Car:
    def __init__(self, pos, width, length, color):
        (self.x, self.y) = pos
        self.width = width
        self.length = length
        self.color = color

        self.speed = 0
        self.acceleration = 0.3
        self.max_speed = 10
        self.friction = 0.02

        self.angle = 0
        self.angular_acc = 0.007

    def update(self, controls):
        self.move(controls)

    def move(self, controls):
        if abs(self.speed) > 0:
            self.speed -= self.friction*self.speed

        if controls["forward"] == True:
            if self.speed + self.acceleration > self.max_speed:
                self.speed = self.max_speed
            else:
                self.speed += self.acceleration
        elif controls["reverse"] == True:
            if self.speed - self.acceleration < -self.max_speed/2:
                self.speed = -self.max_speed/2
            else:
                self.speed -= self.acceleration

        if controls["left"] == True:
            self.angle += self.angular_acc*self.speed
        elif controls["right"] == True:
            self.angle -= self.angular_acc*self.speed

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

    def draw(self, screen):
        poly = self.create_polygon()
        pygame.draw.polygon(screen, self.color, poly)

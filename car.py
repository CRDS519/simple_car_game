import pygame

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
        self.angular_acc = 0.3

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
        if controls["reverse"] == True:
            if self.speed - self.acceleration < -self.max_speed/2:
                self.speed = -self.max_speed/2
            else:
                self.speed -= self.acceleration

        if abs(self.speed) < self.friction:
            self.speed = 0

        self.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x - self.width/2, self.y - self.length/2, self.width, self.length))

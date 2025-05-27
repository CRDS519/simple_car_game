import pygame

class Road:
    def __init__(self, origin, width, line_width, lane_count):
        (self.x, self.y) = origin
        self.width = width
        self.line_width = line_width
        self.lane_count = lane_count
        
        self.infinity = 1000000
        self.left = self.x - self.width/2
        self.right = self.x + self.width/2
        self.top = self.y - self.infinity
        self.bottom = self.y + self.infinity

    def draw_road(self, screen, color):
        pygame.draw.rect(screen, color, pygame.Rect(self.left, self.top, self.width, 2*self.infinity))
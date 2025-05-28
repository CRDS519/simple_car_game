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

        self.margin = 20
        self.dashing = 80

    def get_line_position(self):
        L = []
        r_width = self.width - 2*self.margin - self.line_width
        l_width = int(r_width/self.lane_count)

        for i in range(self.lane_count + 1):
            line_pos = self.left + self.margin + i*l_width
            L.append(line_pos)

        return L

    def draw_road(self, screen, color):
        lines_pos = self.get_line_position()

        pygame.draw.rect(screen, color, pygame.Rect(self.left, self.top, self.width, 2*self.infinity))

        n = 2*self.infinity // self.dashing
        for i in range(self.lane_count + 1):
            if i == 0 or i == self.lane_count:
                pygame.draw.line(screen, 'white', (lines_pos[i], self.top), (lines_pos[i], self.bottom), self.line_width)
            else :
                for j in range(n):
                    if j % 2 == 0:
                        pygame.draw.line(screen, 'white', (lines_pos[i], self.top + j*self.dashing), (lines_pos[i], self.top + (j+1)*self.dashing), self.line_width)
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

        self.borders = [[(self.left + self.margin, self.top), (self.left + self.margin, self.bottom)], [(self.right - self.margin, self.top), (self.right - self.margin, self.bottom)]]

    def get_line_position(self):
        L = []
        r_width = self.width - 2*self.margin - self.line_width
        l_width = int(r_width/self.lane_count)

        for i in range(self.lane_count + 1):
            line_pos = self.left + self.margin + i*l_width
            L.append(line_pos)

        return L

    def draw_road(self, screen, color, camera_y):
        top = self.top - camera_y
        bottom = self.bottom - camera_y

        lines_pos = self.get_line_position()

        pygame.draw.rect(screen, color, pygame.Rect(self.left, top, self.width, bottom - top))

        n = (bottom - top) // self.dashing + 1
        for i in range(self.lane_count + 1):
            x = lines_pos[i]
            if i == 0 or i == self.lane_count:
                pygame.draw.line(screen, 'white', (x, top), (x, bottom), self.line_width)
            else :
                y0 = top
                for j in range(int(n)):
                    if j % 2 == 0:
                        pygame.draw.line(screen, 'white', (x, y0 + j*self.dashing), (x, y0 + (j+1)*self.dashing), self.line_width)
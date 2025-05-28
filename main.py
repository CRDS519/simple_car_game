import pygame
from road import Road

pygame.init()
width = 2560
height = 1600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Car Game')
clock = pygame.time.Clock()
running = True
fps = 60
dt = 1/fps

road = Road((width/2, height/2), 600, 5, 3)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((82,82,82))

    road.draw_road(screen, 'grey')

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
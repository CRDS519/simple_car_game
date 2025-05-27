import pygame

pygame.init()
width = 2560
height = 1600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Car Game')
clock = pygame.time.Clock()
running = True
fps = 60
dt = 1/fps

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill('green')

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
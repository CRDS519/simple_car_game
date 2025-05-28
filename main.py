import pygame
from road import Road
from car import Car

pygame.init()
width = 2560
height = 1600
origin = (width/2, height/2)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Car Game')
clock = pygame.time.Clock()
running = True
fps = 60
dt = 1/fps

controls = {"forward" : False, "reverse" : False, "left" : False, "right": False}

road = Road(origin, 500, 5, 3)
car = Car((width/2, 2*(height/3)), 60, 100, "red")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                controls["forward"] = True
            if event.key == pygame.K_DOWN:
                controls["reverse"] = True
            if event.key == pygame.K_LEFT:
                controls["left"] = True
            if event.key == pygame.K_RIGHT:
                controls["right"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                controls["forward"] = False
            if event.key == pygame.K_DOWN:
                controls["reverse"] = False
            if event.key == pygame.K_LEFT:
                controls["left"] = False
            if event.key == pygame.K_RIGHT:
                controls["right"] = False
    
    screen.fill((82,82,82))

    screen_center_y = 2*height/3
    camera_y = car.y - screen_center_y

    road.draw_road(screen, 'grey', camera_y)
    car.update(controls, dt)
    car.draw(screen, camera_y)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
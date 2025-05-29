import pygame
import random
from road import Road
from car import Car
from utils import *

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

road = Road(origin, 500, 5, 3)
car = Car((road.lane_centers[1], 2*(height/3)), 60, 100, "red", "user", 10)

def generate_traffic_cars(rows, max_cars_per_row, distance_between_rows):
    traffic_cars = []
    for i in range(rows):
        for j in range(max_cars_per_row):
            n = random.randint(0,road.lane_count - 1)
            traffic_cars.append(
                Car((road.lane_centers[n], height/2 - i*distance_between_rows), 60, 100, "blue", "dummy", 6)
            )
    return traffic_cars

traffic = generate_traffic_cars(30, 2, 300)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                car.controls["forward"] = True
            if event.key == pygame.K_DOWN:
                car.controls["reverse"] = True
            if event.key == pygame.K_LEFT:
                car.controls["left"] = True
            if event.key == pygame.K_RIGHT:
                car.controls["right"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                car.controls["forward"] = False
            if event.key == pygame.K_DOWN:
                car.controls["reverse"] = False
            if event.key == pygame.K_LEFT:
                car.controls["left"] = False
            if event.key == pygame.K_RIGHT:
                car.controls["right"] = False
    
    screen.fill((82,82,82))

    screen_center_y = 2*height/3
    camera_y = car.y - screen_center_y

    road.draw_road(screen, 'grey', camera_y)

    traffic_polys = [dcar.poly for dcar in traffic]
    car.update(dt, road.borders, traffic_polys)
    for dcar in traffic:
        dcar.update(dt)

    car.draw(screen, camera_y)
    for dcar in traffic:
        dcar.draw(screen, camera_y)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
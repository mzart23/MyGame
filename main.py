import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('MyGame')
icon = pygame.image.load('img/5440828098166778250.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/peter_targ.png")
target_width = 50
target_height = 50

target_x = random.randint(0,SCREEN_WIDTH-target_width)
target_y = random.randint(0,SCREEN_HEIGHT-target_height)

color = (255,255,255)


running = True
while running:
    pass

pygame.quit()
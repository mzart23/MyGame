import pygame
import random

pygame.init()

SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 1024
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load("img/bg.jpg")

pygame.display.set_caption('MyGame')
icon = pygame.image.load('img/end.png')
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/peter_targ.png")
target_img2 = pygame.image.load("img/loose.png")
target_img3 = pygame.image.load("img/end.png")
target_width = 300
target_height = 300

sound1 = pygame.mixer.Sound("sound/peter.wav")
sound2 = pygame.mixer.Sound("sound/loose.wav")
sound3= pygame.mixer.Sound("sound/end.wav")

pygame.mixer.music.load("sound/kupol.wav")
pygame.mixer.music.play()

target_x = random.randint(0,SCREEN_WIDTH-target_width)
target_y = random.randint(0,SCREEN_HEIGHT-target_height)

target_x2 = random.randint(0,SCREEN_WIDTH-target_width)
target_y2 = random.randint(0,SCREEN_HEIGHT-target_height)

target_x3 = 1536
target_y3 = 1024

color = (255,255,255)
a = 0

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                target_x2 = random.randint(0, SCREEN_WIDTH - target_width)
                target_y2 = random.randint(0, SCREEN_HEIGHT - target_height)
                sound1.play()
            if target_x2 < mouse_x < target_x2 + target_width and target_y2 < mouse_y < target_y2 + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                target_x2 = random.randint(0, SCREEN_WIDTH - target_width)
                target_y2 = random.randint(0, SCREEN_HEIGHT - target_height)
                sound2.play()
                a+=1
            if a == 5:
                target_x3 = 268
                target_y3 = 12
                sound3.play()



    screen.blit(bg, (0, 0))
    screen.blit(target_img2, (target_x2, target_y2))
    screen.blit(target_img, (target_x, target_y))
    screen.blit(target_img3, (target_x3, target_y3))
    pygame.display.update()

pygame.quit()
#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame, sys
from sprites.Bomb_A import Bomb_A
from sprites.Bomb_B import Bomb_B
from sprites.Bomb_C import Bomb_C
from sprites.Tools import Tools
from sprites.Saper import Saper
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700


# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Saper')

WHITE = (255, 255, 255)

all_sprites_list = pygame.sprite.Group()

#walls = [Wall(300,i*100) for i in range(4)] + [Wall(600,i*100+200) for i in range(4)]

#for wall in walls:
#    all_sprites_list.add(wall)

saper = Saper(0,0, WINDOW_WIDTH, WINDOW_HEIGHT)
all_sprites_list.add(saper)

#hans = Hans(300,400, WINDOW_WIDTH, WINDOW_HEIGHT)
#all_sprites_list.add(hans)

Bombs_A = [Bomb_A(0, 200, 300), Bomb_A(900, 100, 400)]
for Bomb_A in Bombs_A:
    all_sprites_list.add(Bomb_A)

Bombs_B = [Bomb_B(200, 300, 400), Bomb_B(500, 400, 1300), Bomb_B(700, 0, 1200)]
for Bomb_B in Bombs_B:
    all_sprites_list.add(Bomb_B)

Bombs_C = [Bomb_C(0, 500, 1200), Bomb_C(300, 400, 900), Bomb_C(600, 0, 500), Bomb_C(800, 150, 900)]
for Bomb_C in Bombs_C:
    all_sprites_list.add(Bomb_C)

background_image = pygame.image.load("images/background.png")
#gameover_image = pygame.image.load("images/gameover.png")
#fail_image = pygame.image.load("images/fail.png")

gamestate = 0

pygame.mixer.init()
#pygame.mixer.music.load('sounds/over.mp3')

#olaf_sound = pygame.mixer.Sound('sounds/olaf.wav')

while True: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                saper.move_right()
            elif event.key == K_LEFT:
                saper.move_left()
            elif event.key == K_DOWN:
                saper.move_down()
            elif event.key == K_UP:
                saper.move_up()
            elif event.key == K_r:
                gamestate = 0
                pygame.mixer.music.stop()

    #hans.move()
    all_sprites_list.update()


    #if pygame.sprite.collide_rect(elsa, hans):
    #    gamestate = 2
    #    elsa.reset()

    for Bomb_A in Bombs_A:
        if pygame.sprite.collide_rect(saper, Bomb_A) or Bomb_A.time == 0:
            all_sprites_list.remove(Bomb_A)
            Bomb_A.rect.x = -1000
            Bomb_A.rect.y = -1000
        Bomb_A.tick()

    for Bomb_B in Bombs_B:
        if pygame.sprite.collide_rect(saper, Bomb_B) or Bomb_B.time == 0:
            all_sprites_list.remove(Bomb_B)
            Bomb_B.rect.x = -1000
            Bomb_B.rect.y = -1000
        Bomb_B.tick()

    for Bomb_C in Bombs_C:
        if pygame.sprite.collide_rect(saper, Bomb_C) or Bomb_C.time == 0:
            all_sprites_list.remove(Bomb_C)
            Bomb_C.rect.x = -1000
            Bomb_C.rect.y = -1000
        Bomb_C.tick()

    if gamestate == 0:
        DISPLAYSURF.blit(background_image, (0,0))
        all_sprites_list.draw(DISPLAYSURF)
    #elif gamestate == 1:
    #    DISPLAYSURF.blit(gameover_image, (0,0))
    #elif gamestate == 2:
    #    DISPLAYSURF.blit(fail_image, (0,0))


    #Refresh Screen
    pygame.display.flip()

    fpsClock.tick(FPS)

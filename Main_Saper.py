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

map = [[Saper(), None, None, None, None, None, None],
       [None, None, None, None, None, None, None],
       [None, None, None, None, None, None, None],
       [None, None, None, None, None, None, None],
       [None, None, None, None, None, None, None],
       [None, None, None, None, None, None, None],
       [None, None, None, None, None, None, None],
       [None, None, None, None, None, None, None],
       [None, None, None, None, None, None, None],
       [None, None, None, None, None, None, None]]

Saper_image = pygame.image.load("images/saper.png")
Saper_x = 0
Saper_y = 0

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Saper')

WHITE = (255, 255, 255)
background_image = pygame.image.load("images/background.png")
gamestate = 0

for i in range(len(map)):
    print("\n")
    for j in range(len(map[i])):
        print(map[i][j])

while True: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                if Saper_x < 9:
                    map[Saper_x + 1][Saper_y] = map[Saper_x][Saper_y]
                    map[Saper_x][Saper_y] = None
                    Saper_x = Saper_x + 1

            elif event.key == K_LEFT:
                if Saper_x > 0:
                    map[Saper_x - 1][Saper_y] = map[Saper_x][Saper_y]
                    map[Saper_x][Saper_y] = None
                    Saper_x = Saper_x - 1

            elif event.key == K_DOWN:
                if Saper_y < 6:
                    map[Saper_x][Saper_y + 1] = map[Saper_x][Saper_y]
                    map[Saper_x][Saper_y] = None
                    Saper_y = Saper_y + 1

            elif event.key == K_UP:
                if Saper_y > 0:
                    map[Saper_x][Saper_y - 1] = map[Saper_x][Saper_y]
                    map[Saper_x][Saper_y] = None
                    Saper_y = Saper_y - 1

        DISPLAYSURF.blit(background_image, (0, 0))
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] is not None:
                    DISPLAYSURF.blit(Saper_image, [i*100, j*100])

    # Refresh Screen
    pygame.display.flip()

    fpsClock.tick(FPS)

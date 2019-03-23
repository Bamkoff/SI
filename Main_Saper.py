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
       [None, Bomb_A(900), None, None, None, None, None],
       [None, None, None, None, None, None, None],
       [None, None, None, None, None, None, None],
       [None, None, None, Bomb_B(800), None, None, None],
       [None, None, None, None, None, None, None],
       [None, None, None, None, None, None, None],
       [Tools(), None, None, None, None, None, None],
       [None, None, None, None, None, Bomb_C(1000), None],
       [None, None, None, None, None, None, None]]

detonated = 0
defused = 0
Saper_image = pygame.image.load("images/saper.png")
Bomb_A_image = pygame.image.load("images/Bomb_A.png")
Bomb_B_image = pygame.image.load("images/Bomb_B.png")
Bomb_C_image = pygame.image.load("images/Bomb_C.png")
Tool_image = pygame.image.load("images/tools.png")
Saper_x = 0
Saper_y = 0

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Saper')

WHITE = (255, 255, 255)
background_image = pygame.image.load("images/background.png")
gamestate = 0

while True: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                if Saper_x < 9:
                    if map[Saper_x + 1][Saper_y] is None:
                        map[Saper_x + 1][Saper_y] = map[Saper_x][Saper_y]
                        map[Saper_x][Saper_y] = None
                        Saper_x = Saper_x + 1

                    elif map[Saper_x + 1][Saper_y].__class__.__name__ == "Tools":
                        map[Saper_x][Saper_y].change_tool()

                    elif map[Saper_x + 1][Saper_y].__class__.__name__ == "Bomb_A":
                        if map[Saper_x][Saper_y].tool == 0:
                            map[Saper_x + 1][Saper_y] = map[Saper_x][Saper_y]
                            map[Saper_x][Saper_y] = None
                            Saper_x = Saper_x + 1
                            defused += 1

                    elif map[Saper_x + 1][Saper_y].__class__.__name__ == "Bomb_B":
                        if map[Saper_x][Saper_y].tool == 1:
                            map[Saper_x + 1][Saper_y] = map[Saper_x][Saper_y]
                            map[Saper_x][Saper_y] = None
                            Saper_x = Saper_x + 1
                            defused += 1

                    elif map[Saper_x + 1][Saper_y].__class__.__name__ == "Bomb_C":
                        if map[Saper_x][Saper_y].tool == 2:
                            map[Saper_x + 1][Saper_y] = map[Saper_x][Saper_y]
                            map[Saper_x][Saper_y] = None
                            Saper_x = Saper_x + 1
                            defused += 1

            elif event.key == K_LEFT:
                if Saper_x > 0:
                    if map[Saper_x - 1][Saper_y] is None:
                        map[Saper_x - 1][Saper_y] = map[Saper_x][Saper_y]
                        map[Saper_x][Saper_y] = None
                        Saper_x = Saper_x - 1

                    elif map[Saper_x - 1][Saper_y].__class__.__name__ == "Tools":
                        map[Saper_x][Saper_y].change_tool()

                    elif map[Saper_x - 1][Saper_y].__class__.__name__ == "Bomb_A":
                        if map[Saper_x][Saper_y].tool == 0:
                            map[Saper_x - 1][Saper_y] = map[Saper_x][Saper_y]
                            map[Saper_x][Saper_y] = None
                            Saper_x = Saper_x - 1
                            defused += 1

                    elif map[Saper_x - 1][Saper_y].__class__.__name__ == "Bomb_B":
                        if map[Saper_x][Saper_y].tool == 1:
                            map[Saper_x - 1][Saper_y] = map[Saper_x][Saper_y]
                            map[Saper_x][Saper_y] = None
                            Saper_x = Saper_x - 1
                            defused += 1

                    elif map[Saper_x - 1][Saper_y].__class__.__name__ == "Bomb_C":
                        if map[Saper_x][Saper_y].tool == 2:
                            map[Saper_x - 1][Saper_y] = map[Saper_x][Saper_y]
                            map[Saper_x][Saper_y] = None
                            Saper_x = Saper_x - 1
                            defused += 1

            elif event.key == K_DOWN:
                if Saper_y < 6:
                    if map[Saper_x][Saper_y + 1] is None:
                        map[Saper_x][Saper_y + 1] = map[Saper_x][Saper_y]
                        map[Saper_x][Saper_y] = None
                        Saper_y = Saper_y + 1

                    elif map[Saper_x][Saper_y + 1].__class__.__name__ == "Tools":
                        map[Saper_x][Saper_y].change_tool()

                    elif map[Saper_x][Saper_y + 1].__class__.__name__ == "Bomb_A":
                        if map[Saper_x][Saper_y].tool == 0:
                            map[Saper_x][Saper_y + 1] = map[Saper_x][Saper_y]
                            map[Saper_x][Saper_y] = None
                            Saper_y = Saper_y + 1
                            defused += 1

                    elif map[Saper_x][Saper_y + 1].__class__.__name__ == "Bomb_B":
                        if map[Saper_x][Saper_y].tool == 1:
                            map[Saper_x][Saper_y + 1] = map[Saper_x][Saper_y]
                            map[Saper_x][Saper_y] = None
                            Saper_y = Saper_y + 1
                            defused += 1

                    elif map[Saper_x][Saper_y + 1].__class__.__name__ == "Bomb_C":
                        if map[Saper_x][Saper_y].tool == 2:
                            map[Saper_x][Saper_y + 1] = map[Saper_x][Saper_y]
                            map[Saper_x][Saper_y] = None
                            Saper_y = Saper_y + 1
                            defused += 1

            elif event.key == K_UP:
                if Saper_y > 0:
                    if map[Saper_x][Saper_y - 1] is None:
                        map[Saper_x][Saper_y - 1] = map[Saper_x][Saper_y]
                        map[Saper_x][Saper_y] = None
                        Saper_y = Saper_y - 1

                    elif map[Saper_x][Saper_y - 1].__class__.__name__ == "Tools":
                        map[Saper_x][Saper_y].change_tool()

                    elif map[Saper_x][Saper_y - 1].__class__.__name__ == "Bomb_A":
                        if map[Saper_x][Saper_y].tool == 0:
                            map[Saper_x][Saper_y - 1] = map[Saper_x][Saper_y]
                            map[Saper_x][Saper_y] = None
                            Saper_y = Saper_y - 1
                            defused += 1

                    elif map[Saper_x][Saper_y - 1].__class__.__name__ == "Bomb_B":
                        if map[Saper_x][Saper_y].tool == 1:
                            map[Saper_x][Saper_y - 1] = map[Saper_x][Saper_y]
                            map[Saper_x][Saper_y] = None
                            Saper_y = Saper_y - 1
                            defused += 1

                    elif map[Saper_x][Saper_y - 1].__class__.__name__ == "Bomb_C":
                        if map[Saper_x][Saper_y].tool == 2:
                            map[Saper_x][Saper_y - 1] = map[Saper_x][Saper_y]
                            map[Saper_x][Saper_y] = None
                            Saper_y = Saper_y - 1
                            defused += 1

        DISPLAYSURF.blit(background_image, (0, 0))
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] is not None:
                    if map[i][j].__class__.__name__ == "Saper":
                        DISPLAYSURF.blit(Saper_image, [i*100, j*100])
                    elif map[i][j].__class__.__name__ == "Bomb_A":
                        if map[i][j].time == 0:
                            map[i][j] = None
                            detonated += 1
                        else:
                            DISPLAYSURF.blit(Bomb_A_image, [i*100, j*100])
                            map[i][j].tick()
                    elif map[i][j].__class__.__name__ == "Bomb_B":
                        if map[i][j].time == 0:
                            map[i][j] = None
                            detonated += 1
                        else:
                            DISPLAYSURF.blit(Bomb_B_image, [i*100, j*100])
                            map[i][j].tick()
                    elif map[i][j].__class__.__name__ == "Bomb_C":
                        if map[i][j].time == 0:
                            map[i][j] = None
                            detonated += 1
                        else:
                            DISPLAYSURF.blit(Bomb_C_image, [i*100, j*100])
                            map[i][j].tick()
                    elif map[i][j].__class__.__name__ == "Tools":
                        DISPLAYSURF.blit(Tool_image, [i * 100, j * 100])

    # Refresh Screen
    pygame.display.flip()

    fpsClock.tick(FPS)

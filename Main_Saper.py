#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame, sys
from sprites.Bomb import Bomb
from sprites.Tools import Tools
from sprites.Saper import Saper
from sprites.Wall import Wall
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

map = [[Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()],
       [Wall(), Tools(), Wall(), None  , Bomb(980, "A"), Wall(), None  , Wall(), Bomb(1260, "B"), None  , None  , None  , None  , Wall()],
       [Wall(), None  , Wall(), None  , Wall(), Wall(), None  , Wall(), Wall(), Wall(), Wall(), Wall(), None  , Wall()],
       [Wall(), None  , Wall(), None  , None  , None  , None  , Wall(), None  , None  , None  , Wall(), None  , Wall()],
       [Wall(), None  , Wall(), Wall(), Wall(), Wall(), None  , Wall(), None  , None  , None, Wall(), None  , Wall()],
       [Wall(), None  , Wall(), Bomb(570, "C"), None  , None  , None  , None  , None  , Wall(), None  , Wall(), None  , Wall()],
       [Wall(), None  , Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), None  , Wall(), None  , Wall(), None  , Wall()],
       [Wall(), None  , None  , None  , None  , None  , None  , Wall(), None  , Wall(), None  , Wall(), None  , Wall()],
       [Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), None  , Wall(), None  , Wall(), None  , None  , None  , Wall()],
       [Wall(), None  , None  , None, None  , None  , None  , Wall(), None  , Wall(), None  , Wall(), Wall(), Wall()],
       [Wall(), None  , Wall(), Wall(), Wall(), None  , None  , None  , Saper(), Wall(), None  , Wall(), None  , Wall()],
       [Wall(), None  , Wall(), Bomb(1060, "A"), Wall(), None  , Wall(), None  , Wall(), Wall(), None  , Wall(), None  , Wall()],
       [Wall(), None  , Wall(), None  , Wall(), None  , Wall(), Wall(), Wall(), None  , None  , None, None  , Wall()],
       [Wall(), None  , Wall(), None  , Wall(), None  , Wall(), Bomb(1130, "C"), Wall(), None  , Wall(), Wall(), None  , Wall()],
       [Wall(), None  , Wall(), None  , Wall(), None  , None  , None  , Wall(), None  , Wall(), None  , None  , Wall()],
       [Wall(), None  , Wall(), None  , Wall(), Wall(), Wall(), Wall(), Wall(), None  , Wall(), None  , Wall(), Wall()],
       [Wall(), None  , Wall(), None  , Wall(), Bomb(1060, "A"), None  , None  , None  , None  , Wall(), None  , None, Wall()],
       [Wall(), None  , Wall(), None  , Wall(), Wall(), Wall(), Wall(), Wall(), None  , Wall(), Wall(), None  , Wall()],
       [Wall(), Bomb(1000, "A"), Wall(), None  , None  , None  , None  , None  , None  , None  , Wall(), Bomb(1100, "B"), None, Wall()],
       [Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()]]

x = 0
y = 0
x_r = 0
y_r = 0

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j].__class__.__name__ == "Saper":
            x = i
            y = j

detonated = 0
defused = 0

Saper_image = pygame.image.load("images/saper.png")
Saper_A_image = pygame.image.load("images/saper_A.png")
Saper_B_image = pygame.image.load("images/saper_B.png")
Saper_C_image = pygame.image.load("images/saper_C.png")
Bomb_A_image = pygame.image.load("images/Bomb_A.png")
Bomb_B_image = pygame.image.load("images/Bomb_B.png")
Bomb_C_image = pygame.image.load("images/Bomb_C.png")
Thumbs_up_image = pygame.image.load("images/Thumbs_up.png")
Hole_image = pygame.image.load("images/Hole.png")
Tool_image = pygame.image.load("images/tools.png")
Wall_image = pygame.image.load("images/Wall.png")


print(len(map))

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Saper')

background_image = pygame.image.load("images/background.png")
gamestate = 0

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                if x < len(map)-1:
                    x_r = x + 1
                    y_r = y

            elif event.key == K_LEFT:
                if x > 0:
                    x_r = x - 1
                    y_r = y

            elif event.key == K_DOWN:
                if y < len(map[0])-1:
                    y_r = y + 1
                    x_r = x

            elif event.key == K_UP:
                if y > 0:
                    y_r = y - 1
                    x_r = x

        if x_r != x or y_r != y:
            if map[x_r][y_r] is None:
                map[x_r][y_r] = map[x][y]
                map[x][y] = None
                x = x_r
                y = y_r

            elif map[x_r][y_r].__class__.__name__ == "Tools":
                map[x][y].change_tool(map[x_r][y_r])
                x_r = x
                y_r = y

            elif map[x_r][y_r].__class__.__name__ == "Bomb":
                defused = map[x][y].defuse(map[x_r][y_r])
                x_r = x
                y_r = y

    DISPLAYSURF.blit(background_image, (0, 0))
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] is not None:
                if map[i][j].__class__.__name__ == "Saper":
                     if map[i][j].tool == "A":
                        DISPLAYSURF.blit(Saper_A_image, [i*50, j*50])

                     elif map[i][j].tool == "B":
                        DISPLAYSURF.blit(Saper_B_image, [i*50, j*50])

                     elif map[i][j].tool == "C":
                        DISPLAYSURF.blit(Saper_C_image, [i*50, j*50])

                     elif map[i][j].tool == "none":
                        DISPLAYSURF.blit(Saper_image, [i*50, j*50])

                elif map[i][j].__class__.__name__ == "Bomb":

                    if map[i][j].time == 0 and map[i][j] != "exploded":
                        map[i][j].type = "exploded"
                        detonated += 1

                    if map[i][j].type == "exploded":
                        DISPLAYSURF.blit(Hole_image, [i * 50, j * 50])

                    elif map[i][j].type == "done":
                        DISPLAYSURF.blit(Thumbs_up_image, [i * 50, j * 50])

                    elif map[i][j].type == "A":
                        DISPLAYSURF.blit(Bomb_A_image, [i * 50, j * 50])

                    elif map[i][j].type == "B":
                        DISPLAYSURF.blit(Bomb_B_image, [i * 50, j * 50])

                    elif map[i][j].type == "C":
                        DISPLAYSURF.blit(Bomb_C_image, [i * 50, j * 50])
                    map[i][j].tick()

                elif map[i][j].__class__.__name__ == "Tools":
                    DISPLAYSURF.blit(Tool_image, [i * 50, j * 50])

                elif map[i][j].__class__.__name__ == "Wall":
                    DISPLAYSURF.blit(Wall_image, [i * 50, j * 50])

    # Refresh Screen
    pygame.display.flip()

    fpsClock.tick(FPS)

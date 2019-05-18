#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame, sys
from sprites.Bomb import Bomb
from sprites.Tools import Tools
from sprites.Saper import Saper
from sprites.Wall import Wall
from pygame.locals import *


Solutions = []

def dfs_find(Grid, Curr_operations, a, b, destination, left, anti_loop):
    dest = destination[:]
    licz = 0
    for i in range(len(dest)):
        if dest[i-licz][0] == a + 1 and dest[i-licz][1] == b:
            dest.pop(i-licz)
            Curr_operations.append("B_R")
            licz = licz + 1
            left = left - 1
        elif dest[i-licz][0] == a - 1 and dest[i-licz][1] == b:
            dest.pop(i-licz)
            Curr_operations.append("B_L")
            licz = licz + 1
            left = left - 1
        elif dest[i-licz][0] == a and dest[i-licz][1] == b - 1:
            dest.pop(i-licz)
            Curr_operations.append("B_U")
            licz = licz + 1
            left = left - 1
        elif dest[i-licz][0] == a and dest[i-licz][1] == b + 1:
            dest.pop(i-licz)
            Curr_operations.append("B_D")
            licz = licz + 1
            left = left - 1

    if left == 0:
        Solutions.append(Curr_operations)
        return 0

    if anti_loop < 80:
        anti_loop = anti_loop + 1
        if Curr_operations[len(Curr_operations) - 1] != "L":
            if Grid[a + 1][b] is None:
                operations1 = Curr_operations[:]
                operations1.append("R")
                dfs_find(Grid, operations1, a + 1, b, dest, left, anti_loop)

        if Curr_operations[len(Curr_operations) - 1] != "R":
            if Grid[a - 1][b] is None:
                operations2 = Curr_operations[:]
                operations2.append("L")
                dfs_find(Grid, operations2, a - 1, b, dest, left,anti_loop)

        if Curr_operations[len(Curr_operations) - 1] != "U":
            if Grid[a][b + 1] is None:
                operations3 = Curr_operations[:]
                operations3.append("D")
                dfs_find(Grid, operations3, a, b + 1, dest, left, anti_loop)

        if Curr_operations[len(Curr_operations) - 1] != "D":
            if Grid[a][b - 1] is None:
                operations4 = Curr_operations[:]
                operations4.append("U")
                dfs_find(Grid, operations4, a, b - 1, dest, left, anti_loop)
        return 0


pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

map = [[Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()],
       [Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Saper(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()],
       [Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), None, Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()],
       [Wall(), Wall(), Wall(), Bomb(980, "A"), Wall(), Wall(), None, Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()],
       [Wall(), Wall(), Wall(), None, Wall(), Wall(), None, Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()],
       [Wall(), Wall(), None, None, None, None, None, None, None, None, None, None, Wall(), Wall()],
       [Wall(), Wall(), None, Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), None, Wall(), Wall()],
       [Wall(), Wall(), None, Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), None, Wall(), Wall()],
       [Wall(), Wall(), None, Wall(), None, Wall(), Wall(), Wall(), Wall(), None, Wall(), None, Wall(), Wall()],
       [Wall(), Wall(), None, Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), None, Wall(), Wall()],
       [Wall(), Wall(), None, Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), None, Wall(), Wall()],
       [Wall(), Wall(), None, Wall(), Wall(), Wall(), Wall(), Wall(), Wall(),Wall(), Wall(), None, Wall(), Wall()],
       [Wall(), Wall(), None, Wall(), None, Wall(), Wall(), Wall(), Wall(), None, Wall(), None, Wall(), Wall()],
       [Wall(), Wall(), None, Wall(), None, Wall(), Wall(), Wall(), Wall(), None, Wall(), None, Wall(), Wall()],
       [Wall(), Wall(), None, Wall(), None, None, None, None, None, None, Wall(), None, Wall(), Wall()],
       [Wall(), Wall(), None, Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), None, Wall(), Wall()],
       [Wall(), Wall(), None, Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), None, Wall(), Wall()],
       [Wall(), Bomb(980, "A"), None, None, None, None, Wall(), None, None, None, None, None, Bomb(980, "A"), Wall()],
       [Wall(), Wall(), Bomb(980, "A"), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()],
	   [Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()]]

x = 0
y = 0
x_r = 0
y_r = 0

dest = []

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j].__class__.__name__ == "Saper":
            x = i
            y = j
        elif map[i][j].__class__.__name__ == "Bomb":
            dest.append([i,j])



dfs_find(map, ["N"], x, y, dest, len(dest), 0)
min_sol = 0
for i in range(len(Solutions)):
    if len(Solutions[i]) < len(Solutions[min_sol]):
        min_sol = i

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

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Saper')

background_image = pygame.image.load("images/background.png")

loop = 1
flaga = 1
while True:
    if loop > len(Solutions[min_sol])-1:
        flaga = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if flaga == 1:
        if Solutions[min_sol][loop] == "R" or  Solutions[min_sol][loop] == "B_R":
            if x < len(map)-1:
                x_r = x + 1
                y_r = y

        elif Solutions[min_sol][loop] == "L" or  Solutions[min_sol][loop] == "B_L":
            if x > 0:
                x_r = x - 1
                y_r = y

        elif Solutions[min_sol][loop] == "D" or  Solutions[min_sol][loop] == "B_D":
            if y < len(map[0])-1:
                y_r = y + 1
                x_r = x

        elif Solutions[min_sol][loop] == "U" or  Solutions[min_sol][loop] == "B_U":
            if y > 0:
                y_r = y - 1
                x_r = x
        loop = loop + 1

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
                defused = defused + map[x][y].defuse(map[x_r][y_r])
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

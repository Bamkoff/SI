#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame, sys, os, random
from sprites.Bomb import Bomb
from sprites.Tools import Tools
from sprites.Saper import Saper
from sprites.Wall import Wall
from pygame.locals import *

def check_type(Grid, x, y):
    if x < 0 or x > len(Grid)-1 or y < 0 or y > len(Grid[0])-1:
        return str(0)
    if Grid[x][y] is None:
        return str(10)
    if Grid[x][y].__class__.__name__ == "Wall":
        return str(1)
    if Grid[x][y].__class__.__name__ == "Bomb":
        if Grid[x][y].type == "done":
            return str(5)
        else:
            return str(50)

def get_surround(Grid, x, y):
    s = ""
    s = s + " | 1x1:." + check_type(Grid, x - 2, y - 2) + " 1x2:." + check_type(Grid, x - 2, y - 1)
    s = s + " 1x3:." + check_type(Grid, x - 2, y) + " 1x4:." + check_type(Grid, x - 2, y + 1)
    s = s + " 1x5:." + check_type(Grid, x - 2, y + 2)

    s = s + " 2x1:." + check_type(Grid, x - 1, y - 2) + " 2x2:." + check_type(Grid, x - 1, y - 1)
    s = s + " 2x3:." + check_type(Grid, x - 1, y) + " 2x4:." + check_type(Grid, x - 1, y + 1)
    s = s + " 2x5:." + check_type(Grid, x - 1, y + 2)

    s = s + " 3x1:." + check_type(Grid, x, y - 2) + " 3x2:." + check_type(Grid, x, y - 1)
    s = s + " 3x4:." + check_type(Grid, x, y + 1) + " 3x5:." + check_type(Grid, x, y + 2)

    s = s + " 4x1:." + check_type(Grid, x + 1, y - 2) + " 4x2:." + check_type(Grid, x + 1, y - 1)
    s = s + " 4x3:." + check_type(Grid, x + 1, y) + " 4x4:." + check_type(Grid, x + 1, y + 1)
    s = s + " 4x5:." + check_type(Grid, x + 1, y + 2)

    s = s + " 5x1:." + check_type(Grid, x + 2, y - 2) + " 5x2:." + check_type(Grid, x + 2, y - 1)
    s = s + " 5x3:." + check_type(Grid, x + 2, y) + " 5x4:." + check_type(Grid, x + 2, y + 1)
    s = s + " 5x5:." + check_type(Grid, x + 2, y + 2)
    return s

def write_to_file(file, string):
    f = open(file, "w")
    f.write(string)
    f.write("\n")
    f.close()

def read_map(file):
    f = open("maps/" + file, "r")
    s = f.read()
    map.append([])
    index = 0
    for i in range(len(s)-1):
        if s[i] == "0":
            map[index].append(None)
        if s[i] == "1":
            map[index].append(Wall())
        if s[i] == "2":
            map[index].append(Saper())
        if s[i] == "3":
            map[index].append(Bomb(random.randint(400, 601), "A"))
        if s[i] == "\n":
            map.append([])
            index = index + 1

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

map = []
read_map("SUPER-SEBA-BY-DUNDAL.txt")

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

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Saper')

background_image = pygame.image.load("images/background.png")

prev_output1 = 0
prev_output2 = 0
counter = 0
flag1 = True
flag2 = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    s = get_surround(map, x, y)
    write_to_file("wabbit_move", s)
    output = float(os.popen("vw -i wabbit_model wabbit_move -p /dev/stdout --quiet").read())
    print(output)

    if prev_output1 == output or prev_output2 == output:
        counter = counter + 1

    if counter > 10:
        counter = 0
        output = random.randint(0,5)

    prev_output2 = prev_output1
    prev_output1 = output


    if output < 1.5:
        if x < len(map)-1:
            x_r = x + 1
            y_r = y

    elif output < 2.5:
        if x > 0:
            x_r = x - 1
            y_r = y

    elif output < 3.5:
        if y < len(map[0])-1:
            y_r = y + 1
            x_r = x
    else:
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

#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame, sys
from sprites.Bomb import Bomb
from sprites.Tools import Tools
from sprites.Saper import Saper
from sprites.Wall import Wall
from pygame.locals import *


Solution = []

def heuristic_cost(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def A_star(Grid, start, dest, priority):
    Closed_set = []
    Open_set = [start]
    cameFrom = []
    gScore = []
    fScore = []
    Grid2 = []
    goal = dest[priority.index(min(priority))]
    dest.pop(priority.index(min(priority)))
    priority.pop(priority.index(min(priority)))

    for i in range(len(Grid)):
        gScore.append([])
        fScore.append([])
        cameFrom.append([])
        Grid2.append([])
        for j in range(len(Grid[i])):
            gScore[i].append(1000)
            fScore[i].append(1000)
            cameFrom[i].append([i, j])
            if Grid[i][j] is None or Grid[i][j].__class__.__name__ == "Saper" or (i == goal[0] and j == goal[1]):
                Grid2[i].append(None)
            else:
                Grid2[i].append(Wall())

    gScore[start[0]][start[1]] = 0
    fScore[start[0]][start[1]] = heuristic_cost(start, goal)
    flag3 = True
    while(len(Open_set)>0) and flag3:
        current = Open_set[0]
        current_id = 0
        for l in range(len(Open_set)):
            if fScore[Open_set[l][0]][Open_set[l][1]] < fScore[current[0]][current[1]]:
                current = Open_set[l]
                current_id = l

        if current[0] == goal[0] and current[1] == goal[1]:
            flag3 = False


        Open_set.pop(current_id)
        Closed_set.append(current)

        for k in range(4):
            flag2 = False
            if k == 0 and Grid2[current[0] + 1][current[1]].__class__.__name__ != "Wall":
                neighbor = [current[0] + 1, current[1]]
                flag2 = True
            if k == 1 and Grid2[current[0] - 1][current[1]].__class__.__name__ != "Wall":
                flag2 = True
                neighbor = [current[0] - 1, current[1]]
            if k == 2 and Grid2[current[0]][current[1] + 1].__class__.__name__ != "Wall":
                flag2 = True
                neighbor = [current[0], current[1] + 1]
            if k == 3 and Grid2[current[0]][current[1] - 1].__class__.__name__ != "Wall":
                flag2 = True
                neighbor = [current[0], current[1] - 1]

            if flag2:
                flag1 = True
                for l in range(len(Closed_set)):
                    if Closed_set[l][0] == neighbor[0] and Closed_set[l][1] == neighbor[1]:
                        flag1 = False

            if flag2 and flag1:
                for l in range(len(Closed_set)):
                    if Closed_set[l][0] == neighbor[0] and Closed_set[l][1] == neighbor[1]:
                        flag2 = False
                if flag2:
                    flag1 = True
                    poss_gScore = gScore[current[0]][current[1]] + 1

                    for l in range(len(Open_set)):
                        if Open_set[l][0] == neighbor[0] and Open_set[l][1] == neighbor[1]:
                            flag1 = False
                    if flag1:
                        Open_set.append(neighbor)
                    elif poss_gScore >= gScore[neighbor[0]][neighbor[1]]:
                        continue

                    cameFrom[neighbor[0]][neighbor[1]] = [current[0], current[1]]
                    gScore[neighbor[0]][neighbor[1]] = poss_gScore
                    fScore[neighbor[0]][neighbor[1]] = gScore[neighbor[0]][neighbor[1]] + heuristic_cost(neighbor, goal)
    Path = []
    temp0 = goal[0]
    temp1 = goal[1]
    Path.append([temp0, temp1])
    while not(temp0 == start[0] and temp1 == start[1]):
        Path.append([cameFrom[temp0][temp1][0],cameFrom[temp0][temp1][1]])
        help1 = temp0
        help2 = temp1
        temp0 = cameFrom[help1][help2][0]
        temp1 = cameFrom[help1][help2][1]

    for i in range(len(Path)-1,-1,-1):
        Solution.append(Path[i])

    if len(dest) > 0:
        A_star(Grid, cameFrom[goal[0]][goal[1]], dest, priority)


pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

map = [[Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()],
	[Wall(), Saper(), None, None, None, None, None, None, None, None, None, None, Bomb(980, "A"), Wall()],
	[Wall(), None, Wall(), Wall(), None, Wall(), Bomb(980, "A"), Wall(), None, Wall(), Wall(), Wall(), None, Wall()],
	[Wall(), None, None, Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), None, None, None, None, Wall()],
	[Wall(), None, None, Wall(), None, None, None, None, None, None, Wall(), None, None, Wall()],
	[Wall(), Wall(), None, Wall(), Wall(), None, Wall(), None, Wall(), Wall(), Wall(), Wall(), None, Wall()],
	[Wall(), None, None, Wall(), None, None, Wall(), None, Wall(), None, Wall(), None, None, Wall()],
	[Wall(), None, Wall(), Wall(), None, Wall(), Wall(), None, Wall(), None, Wall(), None, Wall(), Wall()],
	[Wall(), None, None, Wall(), None, None, None, None, Wall(), None, Wall(), None, None, Wall()],
	[Wall(), Wall(), None, Wall(), None, Wall(), None, None, Wall(), None, Wall(), Wall(), None, Wall()],
	[Wall(), None, None, None, None, Wall(), None, None, Wall(), None, Wall(), None, None, Wall()],
	[Wall(), None, None, Wall(), None, None, None, None, Wall(), None, Wall(), Wall(), Wall(), Wall()],
	[Wall(), None, Wall(), Wall(), Wall(), Wall(), Wall(), None, None, None, Wall(), Bomb(980, "A"), Wall(), Wall()],
	[Wall(), None, Wall(), None, Wall(), None, None, None, Wall(), None, None, None, Wall(), Wall()],
	[Wall(), None, Wall(), None, Wall(), None, None, Wall(), None, None, Wall(), None, None, Wall()],
	[Wall(), None, None, None, Wall(), None, Wall(), None, None, None, Wall(), Wall(), None, Wall()],
	[Wall(), None, Wall(), None, Wall(), None, None, None, Wall(), Wall(), Wall(), Wall(), None, Wall()],
	[Wall(), None, Wall(), None, Wall(), None, Wall(), None, Wall(), Bomb(980, "A"), Wall(), Wall(), None, Wall()],
	[Wall(), Bomb(980, "A"), Wall(), None, None, None, None, Wall(), None, None, None, None, None, Wall()],
	[Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()]]

x = 0
y = 0
x_r = 0
y_r = 0

dest = []
priority = []

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j].__class__.__name__ == "Saper":
            x = i
            y = j
        elif map[i][j].__class__.__name__ == "Bomb":
            dest.append([i,j])
            priority.append(map[i][j].priority())

A_star(map, [x,y], dest, priority)

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

loop = 0

flag = True
while True:
    if loop >= len(Solution)-1:
        flag = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if flag:
        loop = loop + 1
        if map[Solution[loop][0]][Solution[loop][1]] is None:
            map[Solution[loop][0]][Solution[loop][1]] = map[x][y]
            map[x][y] = None
            x = Solution[loop][0]
            y = Solution[loop][1]

        elif map[Solution[loop][0]][Solution[loop][1]].__class__.__name__ == "Tools":
            map[x][y].change_tool(map[Solution[loop][0]][Solution[loop][1]])

        elif map[Solution[loop][0]][Solution[loop][1]].__class__.__name__ == "Bomb":
            defused = defused + map[x][y].defuse(map[Solution[loop][0]][Solution[loop][1]])

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

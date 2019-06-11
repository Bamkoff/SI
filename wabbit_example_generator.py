#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame, sys, os, random, time
from sprites.Bomb import Bomb
from sprites.Tools import Tools
from sprites.Saper import Saper
from sprites.Wall import Wall
from pygame.locals import *


Solution = []
map = []

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

    for i in range(len(Path)-1,0,-1):
        if Path[i][0] + 1 == Path[i-1][0] and Path[i][1] == Path[i-1][1]:
            Solution.append("R")
        elif Path[i][0] - 1 == Path[i-1][0] and Path[i][1] == Path[i-1][1]:
            Solution.append("L")
        elif Path[i][0] == Path[i-1][0] and Path[i][1] + 1 == Path[i-1][1]:
            Solution.append("D")
        elif Path[i][0] == Path[i-1][0] and Path[i][1] - 1 == Path[i-1][1]:
            Solution.append("U")
    for i in range(len(dest)):
        priority[i] = heuristic_cost(cameFrom[goal[0]][goal[1]], dest[i])

    if len(dest) > 0:
        A_star(Grid, cameFrom[goal[0]][goal[1]], dest, priority)

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
    f = open(file, "a")
    f.write(string)
    f.write("\n")
    f.close()

maps = (os.popen("ls maps").read()).split("\n")

x = 0
y = 0
x_r = 0
y_r = 0
loop = 0
counter1 = 0
counter2 = 0
flag = True

while True:
    if loop >= len(Solution):
        loop = 0
        map = []
        read_map(maps[counter1])
        dest = []
        priority = []
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j].__class__.__name__ == "Saper":
                    x = i
                    y = j

        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j].__class__.__name__ == "Bomb":
                    dest.append([i, j])
                    priority.append(heuristic_cost([x, y], [i, j]))

        Solution = []

        A_star(map, [x, y], dest, priority)

        if counter1 >= len(maps)-2:
            counter2 = counter2 + 1
            couter1 = 0
        else:
            counter1 = counter1 + 1

        if counter2 > 100000:
            os.popen("vw wabbit_examples -f wabbit_model")
            time.sleep(5)
            sys.exit()

    s = ""
    if Solution[loop] == "R":
        if x < len(map)-1:
            x_r = x + 1
            y_r = y
            s = "1"

    elif Solution[loop] == "L":
        if x > 0:
            x_r = x - 1
            y_r = y
            s = "3"

    elif Solution[loop] == "D":
        if y < len(map[0])-1:
            y_r = y + 1
            x_r = x
            s = "2"

    elif Solution[loop] == "U":
        if y > 0:
            y_r = y - 1
            x_r = x
            s = "4"

    s = s + get_surround(map,x,y)
    write_to_file("wabbit_examples", s)
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
            map[x][y].defuse(map[x_r][y_r])
            x_r = x
            y_r = y

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j].__class__.__name__ == "Bomb":
                if map[i][j].time == 0 and map[i][j] != "exploded":
                    map[i][j].type = "exploded"
                map[i][j].tick()
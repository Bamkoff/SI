#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *


class Bomb_C():
    def __init__(self, t):

        # Set height, width
#        self.image = pygame.image.load("images/wall.png")

        # Make our top-left corner the passed-in location.
        self.time = t
        self.type = "C"

    def tick(self):
        if self.time > 0:
            self.time = self.time - 1
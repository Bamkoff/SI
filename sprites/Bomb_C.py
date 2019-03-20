#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *


class Bomb_C(pygame.sprite.Sprite):
    def __init__(self, time):
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
#        self.image = pygame.image.load("images/wall.png")
        self.image = pygame.image.load("images/Bomb_C.png")

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.time = time
        self.type = "C"

    def tick(self):
        if self.time > 0:
            self.time = self.time - 1
#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

class Bomb_B(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
#        self.image = pygame.image.load("images/wall.png")
        self.image = pygame.image.load("images/Bomb_B.png")

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

class Tools(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
#       self.image = pygame.image.load("images/wall.png")
        self.image = pygame.image.load("images/tools.png")


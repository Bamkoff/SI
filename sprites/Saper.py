#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *


class Saper(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
        self.image = pygame.image.load("images/saper.png")

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.tool = 1

    def change_tool(self):
        self.tool = self.tool + 1
        self.tool = self.tool % 3
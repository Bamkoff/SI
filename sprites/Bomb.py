#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from pygame.locals import *


class Bomb:
    def __init__(self, time, type):

        self.time = time
        self.type = type

    def tick(self):
        if self.time > 0:
            self.time = self.time - 1

    def priority(self):
        return self.time
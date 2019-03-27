#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from pygame.locals import *


class Tools():
    def __init__(self):
        self.tool = "A"
        self.next_tool = 1

    def change_tool(self):
        if self.next_tool == 1:
            self.tool = "B"
        elif self.next_tool == 2:
            self.tool = "C"
        else:
            self.tool = "A"
        self.next_tool = self.next_tool + 1
        self.next_tool = self.next_tool % 3

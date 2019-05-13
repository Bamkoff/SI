#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from sprites.Tools import Tools
from sprites.Bomb import Bomb
from pygame.locals import *


class Saper():
    def __init__(self):

        self.tool = "A"

    def change_tool(self, tool_box):
        self.tool = tool_box.tool
        tool_box.change_tool()

    def defuse(self, bomb):
        if bomb.type == self.tool and bomb.time > 0:
            bomb.time = -1
            bomb.type = "done"
            return 1
        else:
            return 0
####################################
# Driftwood 2D Game Dev. Suite     #
# widget.py                        #
# Copyright 2014 PariahSoft LLC    #
# Copyright 2016 Michael D. Reiley #
# & Paul Merrill                   #
####################################

# **********
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
# **********

from sdl2 import *


class Widget():

    def __init__(self, manager, t):
        self.manager = manager
        self.wid = -1

        self.active = False
        self.focus = False
        self.type = t
        self.image = None
        self.texture = None
        self.x = 0
        self.y = 0
        self.realx = None
        self.realy = None
        self.width = 0
        self.height = 0
        self.font = None
        self.text = ""
        self.textwidth = None
        self.textheight = None
        self.ptsize = 0
        self.container = None
        self.contains = []

        self.__destroytexture = SDL_DestroyTexture

    def srcrect(self):
        if self.image:
            return (0, 0, self.image.width, self.image.height)
        elif self.texture:
            return (0, 0, self.textwidth, self.textheight)
        return None

    def dstrect(self):
        return (self.realx, self.realy, self.width, self.height)

    def _terminate(self):
        """Cleanup before deletion.
        """
        if self.texture:
            self.__destroytexture(self.texture)
            self.texture = None

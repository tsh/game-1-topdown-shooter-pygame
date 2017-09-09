import pygame
from pygame.locals import *


class Map(object):
    def __init__(self):
        self.size = 100
        self.map = [[1, 0, 1, 0, 1, 0, 2],
                    [0, 1]]

    def render(self, surface):
        for irow, row in enumerate(self.map):
            for icol, tile in enumerate(row):
                r = pygame.Rect(icol*self.size, irow*self.size, self.size, self.size)
                color = "blue"
                if tile == 0:
                    color = "black"
                elif tile == 1:
                    color = "red"
                elif tile == 2:
                    color = "orange"
                surface.fill(Color(color), r)
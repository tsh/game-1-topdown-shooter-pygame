import pygame
from pygame.locals import *


class Map(object):
    def __init__(self):
        self.size = 100
        self.map = [[1, 0, 1, 0, 1, 0, 2],
                    [0, 1]]

    def render(self, wsurface, camera):
        surface = pygame.Surface((1000, 1000))
        surface.fill((255, 255, 255))
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
        x, y = camera.viewport.x, camera.viewport.y
        print ('camera map ', camera.viewport)
        wsurface.blit(surface, (-x, -y))
import pygame
from pygame.locals import *


class Map(object):
    def __init__(self):
        self.size = 100
        self.map = [[1, 0, 1, 0, 1, 0, 2],
                    [0, 1]]

    def render(self, window_surface, camera):
        wrld_size = 1000
        wrld_srf = pygame.Surface((wrld_size, wrld_size))
        wrld_srf.fill((255, 255, 255))
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
                wrld_srf.fill(Color(color), r)
        x = camera.viewport.x if camera.viewport.x > 0 else 0
        y = camera.viewport.y if camera.viewport.y > 0 else 0

        print ('camera map ', camera.viewport)
        window_surface.blit(wrld_srf, (-x, -y))
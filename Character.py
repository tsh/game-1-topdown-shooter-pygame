import pygame
from pygame.locals import *


class Character(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 50

    def render(self, surface):
        r = pygame.Rect(self.x*self.size, self.y*self.size, self.size, self.size)
        pygame.draw.circle(surface, Color("green"), (self.x, self.y), self.size)
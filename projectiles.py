import pygame
from pygame.locals import *


class Projectile(object):
    projectiles = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 5
        self.speed = 3

    def render(self, surface):
        pygame.draw.circle(surface, Color("yellow"), (self.x, self.y), self.size)

    @classmethod
    def update(cls, surface):
        for prj in cls.projectiles:
            prj.x += prj.speed
            prj.y += prj.speed
            prj.render(surface)
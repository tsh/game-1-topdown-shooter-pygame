import pygame
from pygame.locals import *
from pygame.math import Vector2


class Projectile(object):
    projectiles = []

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.size = 5
        self.speed = 3
        self.direction = direction

    def render(self, surface):
        pygame.draw.circle(surface, Color("yellow"), (self.x, self.y), self.size)

    @classmethod
    def update(cls, surface):
        for prj in cls.projectiles:
            prj.x += int(prj.speed * prj.direction.x)
            prj.y += int(prj.speed * prj.direction.y)
            prj.render(surface)
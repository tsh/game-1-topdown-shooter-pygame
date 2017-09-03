import pygame
from pygame.locals import *


class Projectile(object):
    projectiles = []

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.size = 5
        self.speed = 3
        self.direction = direction
        self.remove = False

    def render(self, surface):
        pygame.draw.circle(surface, Color("yellow"), (int(self.x), int(self.y)), self.size)

    @classmethod
    def update(cls, surface):
        for prj in cls.projectiles:
            if prj.remove:
                cls.projectiles.remove(prj)
            else:
                prj.x += prj.speed * prj.direction.x
                prj.y += prj.speed * prj.direction.y
                prj.render(surface)
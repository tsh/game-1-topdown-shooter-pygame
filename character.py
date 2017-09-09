import pygame
from pygame.locals import *
from pygame import Rect
from pymunk.vec2d import Vec2d

from projectiles import Projectile


class Character(object):
    LEFT = 'left'
    RIGHT = 'right'
    FORWARD = 'forward'
    BACKWARD = 'backward'

    def __init__(self):
        self.size = 50
        self.rect = Rect(0, 0, self.size, self.size)
        self.rect.centerx = 0
        self.rect.centery = 0
        self.speed = 10

    def render(self, surface):
        print (self.rect)
        pygame.draw.circle(surface, Color("green"), (self.rect.centerx, self.rect.centery), self.size)

    def move(self, direction):
        if direction == self.LEFT:
            self.rect.centerx -= self.speed
        elif direction == self.RIGHT:
            self.rect.centerx += self.speed
        elif direction == self.FORWARD:
            self.rect.centery -= self.speed
        elif direction == self.BACKWARD:
            self.rect.centery += self.speed

    def shoot(self, surface, direction: Vec2d=None, target: Vec2d=None):
        if direction:
            # shoot in a straight line
            prj = Projectile(self.rect.centerx, self.rect.centery, direction)
        else:
            # shoot in specific target
            target = (target - Vec2d(self.rect.centerx, self.rect.centery)).normalized()
            prj = Projectile(self.rect.centerx, self.rect.centery, target)
        Projectile.projectiles.append(prj)


class Enemy(object):
    def __init__(self):
        self.pos = Vec2d(200, 200)

    def render(self, surface):
        pygame.draw.circle(surface, Color("grey"), self.pos, 10)
import pygame
from pygame.locals import *
from pymunk.vec2d import Vec2d

from projectiles import Projectile


class Character(object):
    LEFT = 'left'
    RIGHT = 'right'
    FORWARD = 'forward'
    BACKWARD = 'backward'

    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 50
        self.speed = 10

    def render(self, surface):
        pygame.draw.circle(surface, Color("green"), (self.x, self.y), self.size)

    def move(self, direction):
        if direction == self.LEFT:
            self.x -= self.speed
        elif direction == self.RIGHT:
            self.x += self.speed
        elif direction == self.FORWARD:
            self.y -= self.speed
        elif direction == self.BACKWARD:
            self.y += self.speed

    def shoot(self, surface, direction: Vec2d):
        direction = (direction - Vec2d(self.x, self.y)).normalized()
        prj = Projectile(self.x, self.y, direction)
        Projectile.projectiles.append(prj)
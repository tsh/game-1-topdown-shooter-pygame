import pygame
from pygame.locals import *


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
        r = pygame.Rect(self.x*self.size, self.y*self.size, self.size, self.size)
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
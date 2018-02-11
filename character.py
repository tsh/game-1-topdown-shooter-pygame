from pygame.locals import *
from pygame import Rect
from pymunk.vec2d import Vec2d

from projectiles import Projectile
from bases import Drawable


class Character(Drawable):
    LEFT = 'left'
    RIGHT = 'right'
    FORWARD = 'forward'
    BACKWARD = 'backward'

    def __init__(self, center_x, center_y):
        self.size = 50
        self.rect = Rect(0, 0, self.size, self.size)
        self.rect.centerx = center_x
        self.rect.centery = center_y
        self.speed = 10
        self.color = Color('Green')

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


class Enemy(Drawable):
    enemies = []

    def __init__(self):
        self.rect = self.rect = Rect(200, 200, 10, 10)
        self.remove = False
        self.color = Color('Grey')
        self.size = 10

    @classmethod
    def draw_all(cls, surface):
        for enemy in cls.enemies:
            enemy.draw(surface)

    @classmethod
    def update(cls):
        for obj in cls.enemies:
            if obj.remove:
                cls.enemies.remove(obj)
import pygame, sys
from pygame import Rect
from pygame.locals import *
from pymunk.vec2d import Vec2d
from map import Map
from character import Character
from projectiles import Projectile


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
UP = Vec2d(0, -1)
DOWN = Vec2d(0, 1)
LEFT = Vec2d(-1, 0)
RIGHT = Vec2d(1, 0)
WIDTH = 500
HEIGHT = 400


class GameObjectManager(object):
    def __init__(self, width, height):
        self.rect = Rect(0, 0, width, height)

    def check_boundry(self):
        # if isinstance(obj, Vec2d):
        for prj in Projectile.projectiles:
            if not self.rect.collidepoint((prj.x, prj.y)):
                prj.remove = True


#Set up pygame
pygame.init()

#Set up the window
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Hello World')

#Set up fonts
basicFont = pygame.font.SysFont(None, 48)
text = basicFont.render('HELLO WORLD', True, BLACK)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

map = Map()
chr = Character()
gom = GameObjectManager(WIDTH, HEIGHT)

clock = pygame.time.Clock()
#Run the game loop
while True:
    clock.tick(60)

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_w]:
        chr.move(chr.FORWARD)
        print('Forward')
    elif key_pressed[pygame.K_s]:
        chr.move(chr.BACKWARD)
        print('Backward')
    elif key_pressed[pygame.K_a]:
        chr.move(chr.LEFT)
        print('Stroll Left')
    elif key_pressed[pygame.K_d]:
        chr.move(chr.RIGHT)
        print('Stroll Right')

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                chr.shoot(windowSurface, direction=UP)
                print('Up')
            elif event.key == pygame.K_DOWN:
                chr.shoot(windowSurface, direction=DOWN)
                print('Down')
            elif event.key == pygame.K_LEFT:
                chr.shoot(windowSurface, direction=LEFT)
                print('Left')
            elif event.key == pygame.K_RIGHT:
                chr.shoot(windowSurface, direction=RIGHT)
                print('Right')
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            chr.shoot(windowSurface, target=Vec2d(pos))
            print(pos)

    windowSurface.fill(WHITE)
    map.render(windowSurface)
    windowSurface.blit(text,textRect)
    chr.render(windowSurface)
    gom.check_boundry()
    print (Projectile.projectiles)
    Projectile.update(windowSurface)
    pygame.display.update()
sys.exit()
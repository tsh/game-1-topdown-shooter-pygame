import pygame, sys
from pygame.locals import *
from pymunk.vec2d import Vec2d
from map import Map
from character import Character
from projectiles import Projectile

#Set up pygame
pygame.init()

#Set up the window
windowSurface = pygame.display.set_mode((500, 400), 0 , 32)
pygame.display.set_caption('Hello World')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
UP = Vec2d(0, -1)
DOWN = Vec2d(0, 1)
LEFT = Vec2d(-1, 0)
RIGHT = Vec2d(1, 0)

#Set up fonts
basicFont = pygame.font.SysFont(None, 48)
text = basicFont.render('HELLO WORLD', True, BLACK)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

map = Map()
chr = Character()

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
                chr.shoot(windowSurface, UP)
                print('Up')
            elif event.key == pygame.K_DOWN:
                chr.shoot(windowSurface, DOWN)
                print('Down')
            elif event.key == pygame.K_LEFT:
                chr.shoot(windowSurface, LEFT)
                print('Left')
            elif event.key == pygame.K_RIGHT:
                chr.shoot(windowSurface, RIGHT)
                print('Right')
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            chr.shoot(windowSurface, Vec2d(pos))
            print(pos)

    windowSurface.fill(WHITE)
    map.render(windowSurface)
    windowSurface.blit(text,textRect)
    chr.render(windowSurface)
    Projectile.update(windowSurface)
    pygame.display.update()
sys.exit()
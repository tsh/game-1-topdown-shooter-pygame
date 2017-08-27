import pygame, sys
from pygame.locals import *
from map import Map
from character import Character
from projectiles import Projectile

#Set up pygame
pygame.init()

#Set up the window
windowSurface = pygame.display.set_mode((500, 400), 0 , 32)
pygame.display.set_caption('Hello World')

#Set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#Set up fonts
basicFont = pygame.font.SysFont(None, 48)

#Set up the text
text = basicFont.render('HELLO WORLD', True, BLACK)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#Draw the white background onto the surface
windowSurface.fill(WHITE)

#Draw the text onto the surface
windowSurface.blit(text,textRect)

map = Map()
map.render(windowSurface)

chr = Character()
# chr.render(windowSurface)

#Draw the window onto the screen
pygame.display.update()

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
                print('Up')
            elif event.key == pygame.K_DOWN:
                chr.shoot(windowSurface)
                print ('Down')
            elif event.key == pygame.K_LEFT:
                print('Left')
            elif event.key == pygame.K_RIGHT:
                print('Right')
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)

    windowSurface.fill(WHITE)
    map.render(windowSurface)
    windowSurface.blit(text,textRect)
    chr.render(windowSurface)
    Projectile.update(windowSurface)
    pygame.display.update()
sys.exit()
import pygame, sys
from pygame.locals import *
from map import Map

#Set up pygame
pygame.init()

#Set up the window
windowSurface = pygame.display.set_mode((500, 400), 0 , 32)
pygame.display.set_caption('Hello World')

#Set up the colors
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
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

r = pygame.Rect(100,100,100,100)
windowSurface.fill(Color("red"), r)

#Draw the text onto the surface
windowSurface.blit(text,textRect)

#Draw the window onto the screen
pygame.display.update()

#Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('Forward')
            elif event.key == pygame.K_s:
                print('Backward')
            elif event.key == pygame.K_a:
                print('Stroll Left')
            elif event.key == pygame.K_d:
                print('Stroll Right')
            elif event.key == pygame.K_UP:
                print('Up')
            elif event.key == pygame.K_DOWN:
                print ('Down')
            elif event.key == pygame.K_LEFT:
                print('Left')
            elif event.key == pygame.K_RIGHT:
                print('Right')
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print (pos)
sys.exit()
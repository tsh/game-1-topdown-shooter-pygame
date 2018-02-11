import pygame, sys
from pygame import Rect
from pygame.locals import *
from pymunk.vec2d import Vec2d
from map import Map
from character import Character, Enemy
from projectiles import Projectile
from camera import Camera


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
UP = Vec2d(0, -1)
DOWN = Vec2d(0, 1)
LEFT = Vec2d(-1, 0)
RIGHT = Vec2d(1, 0)
WIDTH = 500
HEIGHT = 400
HALF_WIDTH = int(WIDTH / 2)
HALF_HEIGHT = int(HEIGHT / 2)


class GameObjectManager(object):
    def __init__(self, width, height):
        self.rect = Rect(0, 0, width, height)

    def check_boundry(self):
        for prj in Projectile.projectiles:
            if not self.rect.collidepoint((prj.x, prj.y)):
                prj.remove = True

            for enemy in Enemy.enemies:
                if enemy.rect.collidepoint((prj.x, prj.y)):
                    enemy.remove = True


class Game(object):
    def __init__(self):
        pygame.init()
        #Set up the window
        self.windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption('Hello World')
        #Set up fonts
        basicFont = pygame.font.SysFont(None, 48)
        self.text = basicFont.render('HELLO WORLD', True, BLACK)
        self.textRect = self.text.get_rect()
        self.textRect.centerx = self.windowSurface.get_rect().centerx
        self.textRect.centery = self.windowSurface.get_rect().centery

        self.map = Map()
        self.chr = Character(HALF_WIDTH, HALF_HEIGHT)
        Enemy.enemies.append(Enemy())
        self.gom = GameObjectManager(WIDTH, HEIGHT)
        self.camera = Camera(WIDTH, HEIGHT)

    def game_loop(self):
        clock = pygame.time.Clock()
        #Run the game loop
        while True:
            clock.tick(60)

            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_w]:
                self.chr.move(self.chr.FORWARD)
                self.camera.viewport.centery -= 10
                print('Forward')
            elif key_pressed[pygame.K_s]:
                self.chr.move(self.chr.BACKWARD)
                self.camera.viewport.centery += 10
                print('Backward')
            elif key_pressed[pygame.K_a]:
                self.chr.move(self.chr.LEFT)
                self.camera.viewport.centerx -= 10
                print('Stroll Left')
            elif key_pressed[pygame.K_d]:
                self.chr.move(self.chr.RIGHT)
                self.camera.viewport.centerx += 10
                print('Stroll Right')

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.chr.shoot(self.windowSurface, direction=UP)
                        print('Up')
                    elif event.key == pygame.K_DOWN:
                        self.chr.shoot(self.windowSurface, direction=DOWN)
                        print('Down')
                    elif event.key == pygame.K_LEFT:
                        self.chr.shoot(self.windowSurface, direction=LEFT)
                        print('Left')
                    elif event.key == pygame.K_RIGHT:
                        self.chr.shoot(self.windowSurface, direction=RIGHT)
                        print('Right')
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.chr.shoot(self.windowSurface, target=Vec2d(pos))
                    print(pos)

            self.map.render(self.windowSurface, self.camera)
            self.windowSurface.blit(self.text ,self.textRect)
            self.chr.draw(self.windowSurface)
            Enemy.update()
            Enemy.draw_all(self.windowSurface)
            self.gom.check_boundry()
            Projectile.update(self.windowSurface)
            pygame.display.update()

            self.camera.move(chr)

game = Game()
game.game_loop()
sys.exit()
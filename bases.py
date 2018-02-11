import pygame


class Drawable(object):
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.rect.centerx, self.rect.centery), self.size)

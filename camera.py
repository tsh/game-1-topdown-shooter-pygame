from pygame import Rect

HALF_WIDTH = 500 / 2
HALF_HEIGHT = 400 / 2


class Camera(object):
    def __init__(self, width, height):
        expected_map_tile = 300
        self.viewport = Rect(0, 0, width + expected_map_tile, height + expected_map_tile)

    def apply(self, target):
        return target.rect.move(self.viewport.topleft)

    def move(self, target):
        # l, t, _, _ = target.rect # l = left,  t = top
        # _, _, w, h = self.viewport
        # self.viewport = Rect(-l + HALF_WIDTH, -t + HALF_HEIGHT, w, h)

        # cx, cy = target.rect.centerx, target.rect.centery
        # r = self.viewport
        # r.centerx = cx
        # r.centery = cy
        # self.viewport = r
        # print (self.viewport)
        pass


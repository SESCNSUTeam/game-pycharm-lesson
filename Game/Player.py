import pygame as pg
from GameObject import GameObject
import Math
import config as c
class Player(GameObject):
    def __init__(self, x, y):
        self.image = pg.image.load("ball.png")
        GameObject.__init__(self, x, y, self.image.get_rect().width, self.image.get_rect().height, [2,2])
        self._right = False
        self._left = False
        self._up = False
        self._down = False
        self.hp = 100
        self.damage = 25
        self.blink_cd = False
        self.blink_timer = 0;
        # self.blink_refresh = pg.event.Event(int, )

    def draw(self,surface):
        surface.blit(self.image, self.bounds)

    def update(self):
        dx = 0
        dy = 0
        if self._up:
            dy = -self.speed[1]
        if self._down:
            dy = self.speed[1]
        if self._right:
            dx = self.speed[0]
        if self._left:
            dx = -self.speed[0]
        self.move(dx,dy)

    def handle(self, key):
        if key == pg.K_a:
            self._left = not self._left
        elif key == pg.K_d:
            self._right = not self._right
        elif key == pg.K_w:
            self._up = not self._up
        elif key == pg.K_s:
            self._down = not self._down
        if key == pg.K_SPACE:
            self.blink_cd = True
            if self._left:
                self.move(-c.blink_distance,0)
            if self._right:
                self.move(c.blink_distance,0)
            if self._up:
                self.move(0,-c.blink_distance)
            if self._down:
                self.move(0,c.blink_distance)
    def shot(self):


        pass
    def mouse_handle(self, type, pos):
        if type == pg.MOUSEBUTTONDOWN:
            print("down ", pos)
        elif type == pg.MOUSEBUTTONUP:
            print("up ",pos)
        elif type == pg.MOUSEMOTION:
            print(pos)
        pass
    def refresh_blink(self):
        blink_cd = False
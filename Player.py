import pygame as pg
from GameObject import GameObject

class Player(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y, self.image.get_rect().width, self.image.get_rect().height)
        self.right = False
        self.left = False
        self.up = False
        self.down = False


    def __new__(cls, *args, **kwargs):
        cls.image = pg.image.load("ball.png")
    def get_rect(self):
        return self.bounds

    def draw(self,surface):
        surface.blit(self.image, self.bounds)

    def update(self):
        if self.up:
            dy = -1
        if self.down:
            dy = 1
        if self.right:
            dx = 1
        if self.left:
            dx = -1
        move(dx,dy)

    def handle(self, key):
        if key == pg.K_LEFT:
            if self.right:
                self.right = False

            self.left = not self.left

        elif key == pg.K_RIGHT:
            if self.left:
                self.left = False

            self.right = not self.right

        elif key == pg.K_UP:
            if self.down:
                self.down = False

            self.up = not self.up

        elif key == pg.K_DOWN:
            if self.up:
                self.up = False

            self.down = not self.down
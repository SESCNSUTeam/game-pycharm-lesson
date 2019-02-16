import pygame


class CommonGameObject(pygame.sprite.Sprite):

    ID = 0

    def __init__(self, x, y, w=0, h=0):
        pygame.sprite.Sprite.__init__(self)
        self.global_rect = pygame.Rect(x, y, w, h)
        self.ID = 0

    @property
    def center(self):
        return self.global_rect.center

    @property
    def centerx(self):
        return self.global_rect.centerx

    @property
    def centery(self):
        return self.global_rect.centery

    @property
    def x(self):
        return self.global_rect.left

    @property
    def y(self):
        return self.global_rect.top

    @property
    def w(self):
        return self.global_rect.width

    @property
    def h(self):
        return self.global_rect.height

    @x.setter
    def x(self, value):
        self.global_rect.left = value

    @y.setter
    def y(self, value):
        self.global_rect.top = value

    @classmethod
    def instant(cls, x, y, w=0, h=0):
        cgo = cls(x, y, w, h)
        cgo.ID = cls.ID
        cls.ID += 1
        return cgo
import pygame


class CommonGameObject(pygame.sprite.Sprite):

    class_id = 0
    Id = 0

    def __init__(self, x, y, w=0, h=0):
        pygame.sprite.Sprite.__init__(self)
        self.global_rect = pygame.Rect(x, y, w, h)
        self.id = -1

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

    @property
    def right(self):
        return self.global_rect.right

    @property
    def bottom(self):
        return self.global_rect.bottom

    @property
    def left(self):
        return self.x

    @property
    def top(self):
        return self.y

    @x.setter
    def x(self, value):
        self.global_rect.left = value

    @y.setter
    def y(self, value):
        self.global_rect.top = value

    @w.setter
    def w(self, value):
        self.global_rect.width = value

    @h.setter
    def h(self, value):
        self.global_rect.height = value

    @left.setter
    def left(self, value):
        self.x = value

    @top.setter
    def top(self, value):
        self.y = value

    @right.setter
    def right(self, value):
        self.global_rect.right = value

    @bottom.setter
    def bottom(self, value):
        self.global_rect.bottom = value

    @classmethod
    def instant(cls, x, y, w=0, h=0):
        cgo = cls(x, y, w, h)
        cgo.id = CommonGameObject.Id
        CommonGameObject.Id += 1
        return cgo
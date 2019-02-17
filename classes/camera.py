import pygame
from classes.CommonGameObject import CommonGameObject


class Camera(CommonGameObject):

    def __init__(self, size):
        CommonGameObject.__init__(self, 0, 0, size[0], size[1])

    def apply(self, targets):
        for target in targets:
            target.rect = pygame.Rect(target.x - self.x, target.y - self.y, target.rect.width, target.rect.height)

    def update(self, target):
        self.x = target.centerx - self.w / 2
        self.y = target.centery - self.h / 2

    def set_size(self, size=(1280, 720)):
        self.w = size[0]
        self.h = size[1]

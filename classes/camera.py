import pygame
from classes.CommonGameObject import CommonGameObject


class Camera(CommonGameObject):

    def __init__(self, width, height):
        CommonGameObject.__init__(self, 0, 0)
        self.width = width
        self.height = height

    def apply(self, targets):
        for target in targets:
            target.rect = pygame.Rect(target.x - self.x, target.y - self.y, target.rect.width, target.rect.height)

    def update(self, target):
        self.x = target.x - self.width / 2 + target.rect.width / 2
        self.y = target.y - self.height / 2 + target.rect.height / 2

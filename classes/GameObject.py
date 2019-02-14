import pygame
from classes.CommonGameObject import CommonGameObject


def load_image(image):
    try:
        image = pygame.image.load(image)
    except pygame.error as message:
        print('Cannot load image:', image)
        raise SystemExit(message)
    image = image.convert()
    return image


class ClientGameObject(CommonGameObject):

    def __init__(self, x, y, image="..\\client\\resources\\dog2.jpg"):
        CommonGameObject.__init__(self, x, y)
        self.image = load_image(image)
        self.rect = self.image.get_rect()

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


class Wall(CommonGameObject):

    def __init__(self, x, y, w, h):
        CommonGameObject.__init__(self, x, y)
        self.image = pygame.Surface((w, h))
        self.image.fill((34, 34, 34))
        self.rect = pygame.Rect(0, 0, w, h)


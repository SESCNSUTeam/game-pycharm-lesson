import pygame
from classes.CommonGameObject import CommonGameObject


def load_image(image):
    try:
        image = pygame.image.load(image)
    except pygame.error as message:
        print('Cannot load image:', image)
        raise SystemExit(message)
    image = image.convert()
    return image, image.get_rect()


class ClientGameObject(CommonGameObject):

    def __init__(self, x, y, image):
        CommonGameObject.__init__(self, x, y)
        self.image, self.rect = load_image(image)

    def move(self, dx, dy):
        self.x += dx
        self.y -= dy
        self.rect.move_ip(dx, dy)
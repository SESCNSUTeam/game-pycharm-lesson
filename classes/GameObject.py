import sys

import pygame
import classes.config as c
from classes.CommonGameObject import CommonGameObject
import pygame.math


<<<<<<< HEAD
unload_img = "..//client//resources//green.png"
=======
unload_img = "client\\resources\\green.png"
image_dict = {0: unload_img, 1: unload_img, 2: unload_img, 3: unload_img, 4: unload_img}
>>>>>>> 20c135e237d874e6237d56ea50cb6ff853e52ae3


def load_image(image):
    try:
        image = pygame.image.load(image)
    except pygame.error as message:
        print('Cannot load image:', image)
        raise SystemExit(message)
    image = image.convert()
    return image


class ClientGameObject(CommonGameObject):

    def __init__(self, x, y, class_id):
        image = image_dict[class_id]
        CommonGameObject.__init__(self, x, y)
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.global_rect.size = self.rect.size
        self.isAlive = True


class ServerGameObject(CommonGameObject):

    class_id = 1

    def __init__(self, x, y, w=0, h=0):
        CommonGameObject.__init__(self, x, y, w, h)
        self.isAlive = True
        self.rect = self.global_rect

    def update(self, *args):
        pass

    def on_collision(self, obj):
        pass

    @property
    def info(self):
        return self.id, (self.x, self.y, 0), self.class_id


class SimpleMob(ServerGameObject):

    class_id = 2

    def __init__(self, x, y, w, h):
        ServerGameObject.__init__(self, x, y, w, h)
        self.speed = [1, 0]
        self.changed = False

    def _move(self, dx, dy):
        self.global_rect.move_ip(dx, dy)

    def update(self, dt):
        if self.left < 0:
            self.speed[0] = 1
        elif self.right > 600:
            self.speed[0] = -1
        self._move(self.speed[0], 0)
        self.changed = True


class Wall(ClientGameObject):

    class_id = -1

    def __init__(self, x, y, w, h):
        ClientGameObject.__init__(self, x, y, 2)
        self.image = pygame.Surface((w, h))
        self.image.fill((34, 34, 34))
        self.global_rect = pygame.Rect(x, y, w, h)




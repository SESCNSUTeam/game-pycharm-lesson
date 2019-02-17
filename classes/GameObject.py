import sys

import pygame
import classes.config as c
from classes.CommonGameObject import CommonGameObject
import pygame.math


unload_img = "client\\resources\\green.png"


def load_image(image):
    try:
        image = pygame.image.load(image)
    except pygame.error as message:
        print('Cannot load image:', image)
        raise SystemExit(message)
    image = image.convert()
    return image


class ClientGameObject(CommonGameObject):

    def __init__(self, x, y, image=unload_img):
        CommonGameObject.__init__(self, x, y)
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.global_rect.size = self.rect.size
        self.isAlive = True


class ServerGameObject(CommonGameObject):

    def __init__(self, x, y, w=0, h=0):
        CommonGameObject.__init__(x, y, w, h)
        self.isAlive = True

    def update(self, *args):
        pass

    def on_collision(self, obj):
        pass


class Player(ClientGameObject):
    def __init__(self, x, y):
        ClientGameObject.__init__(self, x, y)
        self._left = False
        self._right = False
        self._up = False
        self._down = False
        self.speed = c.player_speed/1000

    def update(self, dt):
        if self._up:
            self.move(0, -self.speed*dt)
        if self._down:
            self.move(0, self.speed*dt)
        if self._right:
            self.move(self.speed*dt, 0)
        if self._left:
            self.move(-self.speed*dt, 0)

    def handler(self, key):
        if key == pygame.K_w:
            self._up = not self._up
        if key == pygame.K_a:
            self._left = not self._left
        if key == pygame.K_d:
            self._right = not self._right
        if key == pygame.K_s:
            self._down = not self._down
        if key == pygame.K_ESCAPE:
            sys.exit()

    def set_controller(self, client):
        client.keydown_handlers[pygame.K_w].append(self.handler)
        client.keydown_handlers[pygame.K_s].append(self.handler)
        client.keydown_handlers[pygame.K_a].append(self.handler)
        client.keydown_handlers[pygame.K_d].append(self.handler)

        client.keyup_handlers[pygame.K_w].append(self.handler)
        client.keyup_handlers[pygame.K_s].append(self.handler)
        client.keyup_handlers[pygame.K_a].append(self.handler)
        client.keyup_handlers[pygame.K_d].append(self.handler)

        client.keyup_handlers[pygame.K_ESCAPE].append(self.handler)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


class Wall(ClientGameObject):

    def __init__(self, x, y, w, h):
        ClientGameObject.__init__(self, x, y)
        self.image = pygame.Surface((w, h))
        self.image.fill((34, 34, 34))
        self.global_rect = pygame.Rect(x, y, w, h)

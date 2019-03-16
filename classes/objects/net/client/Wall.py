import pygame

from classes.objects.net.client.ClientGameObject import ClientGameObject


class Wall(ClientGameObject):

    class_id = -1

    def __init__(self, x, y, w, h):
        ClientGameObject.__init__(self, x, y, 2)
        self.image = pygame.Surface((w, h))
        self.image.fill((34, 34, 34))
        self.global_rect = pygame.Rect(x, y, w, h)
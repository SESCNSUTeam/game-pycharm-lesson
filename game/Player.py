from pygame.rect import Rect
from Game.game.GameObject import GameObject
import pygame


class Player(GameObject):

    def __init__(self, x, y, image, speed=(0, 0), acceleration=(0, 0)):
        self.image = pygame.image.load(image)
        GameObject.__init__(self, x, y, self.image.get_width(), self.image.get_height(), speed, acceleration)

    def draw(self, surface):
        surface.blit(self.image,self.bounds)

    def update(self, dt):
        pass
from GameObject import GameObject
import pygame

class Mob(GameObject):
    def __init__(self,x,y, damage):
        self.image = pygame.image.load("green.png")
        GameObject.__init__(self, x, y, self.image.get_width(), self.image.get_height(), [0,0])
        self.damage = damage

    def update(self, player):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.bounds)

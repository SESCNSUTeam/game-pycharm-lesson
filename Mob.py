import pygame
from GameObject import GameObject
class Mob(GameObject):
    def __init__(self, x, y, image_dir, damage, hitpoints, speed = (1,1)):
        self.image = pygame.image.load(image_dir)
        self.hp = hitpoints
        self.damage = damage
        GameObject.__init__(self, x, y, self.image.get_width(), self.image.get_height(), speed)

    def update(self, objects,dt):
        for o in objects:
            if o == self:
                continue
            if(self.bounds.colliderect(o.bounds)):
                o.onCollision(self)
                self.onCollision(o)

    def draw(self,surface):
        surface.blit(self.image, self.bounds)

    def onCollision(self,object):
        pass
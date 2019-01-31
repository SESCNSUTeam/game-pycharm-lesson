import pygame
from GameObject import GameObject
class Mob(GameObject):
    def __init__(self, x, y, image_dir, damage, hitpoints, collision = True, speed = (1,1)):
        self.collision = True
        self.image = pygame.image.load(image_dir)
        self.hp = hitpoints
        self.damage = damage
        GameObject.__init__(self, x, y, self.image.get_width(), self.image.get_height(), speed)

    def update(self, dt, objects = []):
        if not self.isDisabled:
            for o in objects:
                if self.bounds.colliderect(o.bounds):
                    self.isDisabled = True
        else:
            pass

    def draw(self,surface):
        surface.blit(self.image, self.bounds)

    def onCollision(self, object):
        if self.collision:
            pass
        else:
            pass
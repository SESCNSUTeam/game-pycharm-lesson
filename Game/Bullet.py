import pygame as pg
import config
class Bullet(GameOjbect):
    def __init__(self,x,y, speed, damage):
        self.image = config.tex_bullet
        GameObject.__init__(self, x, y, self.image.get_rect().width, self.image.get_rect().height, speed)
        self.damage = damage

    def update(self):
        self.pos.x += self.speed[0]
        self.pos.y += self.speed[1]

    def draw(self, surface):
        surface.blit(self.image, self.bounds)

from GameObject import GameObject
import config as c
import pygame as pg
from random import randint
class Brick(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y, c.brick_width, c.brick_height)
        self.colour = randint(0,255), randint(0,255), randint(0,255)
    def draw(self,surface):
        pg.draw.rect(surface, self.colour, self.bounds)
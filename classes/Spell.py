import pygame
from GameObject import GameObject


class Spell:
    def __init__(self, wizard, target, effect = None):
        self.target = target
        self.wizard = wizard
        self.action()
        self.effect = effect
        self.timer = 10000 #mls

    def update(self):
        pass

    def draw(self, surface):
        self.effect.draw(surface)

    def isTimeRemaning(self):
        if self.timer <=0:
            return True
        else:
            return False
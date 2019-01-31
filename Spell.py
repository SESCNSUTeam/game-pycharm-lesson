import pygame
from GameObject import GameObject


class Spell:
    def __init__(self, wizard, target, effect = None):
        self.target = target
        self.wizard = wizard
        self.action()
        self.effect = effect

    def action(self):
        pass

    def update(self):
        pass

    def draw(self, surface):
        self.effect.draw(surface)

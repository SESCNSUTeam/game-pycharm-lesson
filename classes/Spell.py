import pygame
from classes.GameObject import *


class Spell:
    def __init__(self, caster, target):
        self.caster = caster
        self.target = target

    def update(self, dt):
        pass

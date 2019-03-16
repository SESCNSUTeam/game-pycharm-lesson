import copy
import pygame

from classes.magic.Effect import Push, Pull, Hurt


class Spell:
    def __init__(self, caster):
        self.spell_name = None
        self.caster = caster
        self.buffs = []

    def cast_spell(self, world, pos):
        for obj in world.objects:
            if obj.rect.collidepoint(pos):
                effects = []
                for effect in self.buffs:
                    effects.append(copy.copy(effect))
                obj.buff(effects)

    @property
    def name(self):
        return self.spell_name

    @name.setter
    def name(self, value):
        self.spell_name = value


class Throw(Spell):
    def __init__(self, caster):
        super().__init__(caster)
        self.buffs.append(Push(caster))
        self.spell_name = 'throw'


class Grab(Spell):
    def __init__(self, caster):
        super().__init__(caster)
        self.buffs.append(Pull(caster))
        self.spell_name = 'grab'


class Strike(Spell):
    def __init__(self, caster):
        super().__init__(caster)
        self.buffs.append(Hurt(caster))
        self.spell_name = 'strike'
        self.rect = pygame.Rect(0, 0, 16, 16)


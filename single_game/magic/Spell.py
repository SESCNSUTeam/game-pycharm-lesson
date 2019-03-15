import copy
import pygame

from single_game.magic.Effect import Push, Pull, Hurt


class Spell:
    def __init__(self, caster):
        self.name = None
        self.caster = caster
        self.buffs = []

    def cast_spell(self, world, pos):
        for obj in world.objects:
            if obj.rect.collidepoint(pos):
                effects = []
                for effect in self.buffs:
                    effects.append(copy.copy(effect))
                obj.buff(effects)


class Throw(Spell):
    def __init__(self, caster):
        super().__init__(caster)
        self.buffs.append(Push(caster))
        self.name = 'throw'


class Grab(Spell):
    def __init__(self, caster):
        super().__init__(caster)
        self.buffs.append(Pull(caster))
        self.name = 'grab'


class Strike(Spell):
    def __init__(self, caster):
        super().__init__(caster)
        self.buffs.append(Hurt(caster))
        self.name = 'strike'
        self.rect = pygame.Rect(0, 0, 16, 16)

    # def cast_spell(self, world, pos):
    #     self.rect.x = pos[0]
    #     self.rect.y = pos[1]
    #     for obj in world.objects:
    #         if self.rect.colliderect(obj.rect):

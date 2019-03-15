import copy

import classes.config as config

from classes.CommonGameObject import CommonGameObject
from single_game.magic.Effect import Push


def object_by_id(entity_id):
    if entity_id == 1:
        return 'player'
    elif entity_id == 2:
        return 'brick'
    else:
        return None


class Object(CommonGameObject):
    def __init__(self, x, y, w, h, world):
        CommonGameObject.__init__(self, x, y, w, h)

        self.team = 'world'
        self.type = 'object'

        self.is_disabled = False
        self.effects = []
        self.is_collide = True
        self.weight = 1

        self._left = False
        self._right = False
        self._up = False
        self._down = False

        self.hp = 100
        self.world = world

    def update_effects(self, dt):
        for effect in self.effects:
            if not effect.is_alive:
                effect.kill(self.effects)
                continue
            effect.update(target=self, dt=dt)

    def update(self, dt):
        self.update_effects(dt)
        self.is_alive()

    def buff(self, effects=None):
        if effects is None:
            effects = []
        self.effects += effects

    def on_collision(self, object):
        # if not object == self:
        #     effect = Force(self)
        #     object.buff([effect])
        pass

    def is_alive(self):
        if self.hp <= 0:
            self.kill()
            del self


class Brick(Object):
    def __init__(self, x, y, world):
        Object.__init__(self, x, y, config.brick_width, config.brick_height, world)
        self.image = config.brick_image
        self.rect = self.image.get_rect()
        self.weight = 48*16

    def update(self, dt):
        super().update(dt)

    def on_collision(self, object):
        effect = Push(self)
        effect.timer = 100
        object.buff([effect])


class Bullet(Object):
    def __init__(self, owner, pos, world):
        super().__init__(0, 0, config.bullet_width, config.bullet_height, world)

        self.image = config.bullet_image
        self.rect = self.image.get_rect()

        self.speed = 1024/1000

        self.damage = 1

        self.owner = owner

        self.alive_time = 3000

        dx = copy.copy(pos[0]) - copy.copy(self.owner.rect.centerx)
        dy = copy.copy(pos[1]) - copy.copy(self.owner.rect.centery)

        self.global_rect.centerx = copy.copy(self.owner.global_rect.centerx)
        self.global_rect.centery = copy.copy(self.owner.global_rect.centery)

        hyp = (dx * dx + dy * dy) ** (1 / 2)
        self.sin = (dy / hyp)
        self.cos = (dx / hyp)

    def update(self, dt):
        super().update(dt)

        self.move_center(self.speed * self.cos * dt, self.speed * self.sin * dt)
        self.alive_time -= dt
        if self.alive_time <= 0:
            self.kill()
            del self

    def on_collision(self, object):
        '''Со стреляющим не сталкиваемся'''
        if object != self.owner:
            '''Не сталкиваемся с друзьями стреляющего'''
            if object.team != self.owner.team:
                object.hp -= self.damage
                self.kill()
                del self

import pygame

from classes.CommonGameObject import CommonGameObject
import classes.config as config
from single_game.events import spell_request
from single_game.magic.Effect import Push
from single_game.magic.Spell import Throw, Grab


class Object(CommonGameObject):
    def __init__(self, x, y, w, h, is_collide=True):
        super().__init__(x, y, w, h)
        self.is_collide = is_collide
        self.is_disabled = False
        self.effects = []

    def update_effects(self, dt):
        for effect in self.effects:
            if not effect.is_alive:
                effect.kill(self.effects)
                continue
            effect.update(target=self, dt=dt)

    def update(self, dt):
        pass

    def buff(self, effects=None):
        if effects is None:
            effects = []
        self.effects += effects

    def on_collision(self, object):
        speed = object.w*object.h
        effect = Push(self)
        effect.speed = speed
        object.buff([effect])


class Brick(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y, config.brick_width, config.brick_height)
        self.image = config.brick_image
        self.rect = self.image.get_rect()

    def update(self, dt):
        self.update_effects(dt)


class Player(Object):
    def __init__(self, x, y):
        Object.__init__(self, x, y, config.player_width, config.player_width)

        self._left = False
        self._right = False
        self._up = False
        self._down = False
        self.speed = config.player_speed / 1000
        self.acceleration = False

        self.image = config.player_image
        self.rect = self.image.get_rect()
        self.spell_list = []
        self.spell_list.append(Throw(self))
        self.spell_list.append(Grab(self))
        self.curr_spell = 0

    def update(self, dt):
        self.update_effects(dt)
        if not self.is_disabled:
            speed = self.speed
            if self.acceleration:
                speed *= 2
            if self._up:
                self.move(0, -speed * dt)
            if self._down:
                self.move(0, speed * dt)
            if self._right:
                self.move(speed * dt, 0)
            if self._left:
                self.move(-speed * dt, 0)

    def handle(self, key):
        if key == pygame.K_w:
            self._up = not self._up
        if key == pygame.K_a:
            self._left = not self._left
        if key == pygame.K_d:
            self._right = not self._right
        if key == pygame.K_s:
            self._down = not self._down
        if key == pygame.K_LSHIFT:
            self.acceleration = not self.acceleration
        if key == pygame.K_c:
            if self.curr_spell < len(self.spell_list) - 1:
                self.curr_spell += 1
                print(self.spell_list[self.curr_spell].name)
            else:
                self.curr_spell = 0
                print(self.spell_list[self.curr_spell].name)

    def mouse_handler(self, pos, button):
        if button == 1:
            spell_request(self.spell_list[self.curr_spell], pos)
        elif button == 3:
            pass

    def set_controller(self, keydown_handler, keyup_handler, mouse_handlers):
        keydown_handler[pygame.K_w].append(self.handle)
        keydown_handler[pygame.K_s].append(self.handle)
        keydown_handler[pygame.K_a].append(self.handle)
        keydown_handler[pygame.K_d].append(self.handle)
        keydown_handler[pygame.K_LSHIFT].append(self.handle)
        keydown_handler[pygame.K_c].append(self.handle)

        keyup_handler[pygame.K_w].append(self.handle)
        keyup_handler[pygame.K_s].append(self.handle)
        keyup_handler[pygame.K_a].append(self.handle)
        keyup_handler[pygame.K_d].append(self.handle)
        keyup_handler[pygame.K_LSHIFT].append(self.handle)

        mouse_handlers.append(self.mouse_handler)

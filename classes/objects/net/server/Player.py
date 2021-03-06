import pygame

from classes.events import spell_request
from classes.images import collide_sprite
from classes.magic.Spell import Throw, Grab
from classes.objects.net.server.ServerGameObject import ServerGameObject
import classes.gameconsts as config
import classes.idconfig as idconfig
from classes.objects.net.server.Weapon import Weapon


class Player(ServerGameObject):

    class_id = idconfig.id_player

    def __init__(self, x, y, world):
        super().__init__(x, y, config.width_player, config.width_player, world)

        self.team = 'player'
        self.weight = 16 * 16
        self.speed = config.player_speed / 1000
        self.acceleration = False

        self.spell_list = []
        self.spell_list.append(Throw(self))
        self.spell_list.append(Grab(self))
        self.curr_spell = 0

        self.mouse_pos = (0, 0)

        self.weapon = Weapon(self)

        self.hp = 5

        self._fire = False

    def set_mouse_pos(self, pos):
        self.mouse_pos = pos

    def update(self, dt):
        super().update(dt)
        collide_list = collide_sprite(self, self.world.objects, has_sprite=True)

        for obj in collide_list:
            obj.on_collision(self)
        '''Обновление оружия'''
        self.weapon.update(dt)

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
            if self._fire:
                self.weapon.shoot(self.mouse_pos)

    def handle(self, key, is_down):
        if key == pygame.K_w:
            self._up = is_down
        if key == pygame.K_a:
            self._left = is_down
        if key == pygame.K_d:
            self._right = is_down
        if key == pygame.K_s:
            self._down = is_down
        if key == pygame.K_LSHIFT:
            self.acceleration = not self.acceleration
        if key == pygame.K_c:
            if self.curr_spell < len(self.spell_list) - 1:
                self.curr_spell += 1
                print(self.spell_list[self.curr_spell].name)
            else:
                self.curr_spell = 0
                print(self.spell_list[self.curr_spell].name)

    def mouse_handler(self, button, is_down):
        if button == 1:
            spell_request(self.spell_list[self.curr_spell], self.mouse_pos)
        elif button == 3:
            self._fire = is_down

    def set_controller(self, key_down_handler, key_up_handler, mouse_handlers):
        key_down_handler[pygame.K_w].append(self.handle)
        key_down_handler[pygame.K_s].append(self.handle)
        key_down_handler[pygame.K_a].append(self.handle)
        key_down_handler[pygame.K_d].append(self.handle)
        key_down_handler[pygame.K_LSHIFT].append(self.handle)
        key_down_handler[pygame.K_c].append(self.handle)

        key_up_handler[pygame.K_w].append(self.handle)
        key_up_handler[pygame.K_s].append(self.handle)
        key_up_handler[pygame.K_a].append(self.handle)
        key_up_handler[pygame.K_d].append(self.handle)
        key_up_handler[pygame.K_LSHIFT].append(self.handle)

        mouse_handlers.append(self.mouse_handler)

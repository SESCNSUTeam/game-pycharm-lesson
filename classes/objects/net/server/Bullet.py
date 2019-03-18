import copy
import pygame

from classes.sprites import collide_sprite
from classes.objects.net.server.ServerGameObject import ServerGameObject
import classes.gameconsts as gameconsts
import classes.idconfig as idconfig


class Bullet(ServerGameObject):

    class_id = idconfig.id_bullet

    def __init__(self, owner, pos, world):
        super().__init__(0, 0, gameconsts.width_bullet, gameconsts.height_bullet, world)

        self.speed = 1024/1000

        self.damage = 1

        self.owner = owner
        self.team = owner.team

        self.alive_time = 1000

        dx = copy.copy(pos[0]) - copy.copy(self.owner.global_rect.centerx)
        dy = copy.copy(pos[1]) - copy.copy(self.owner.global_rect.centery)

        self.global_rect.centerx = copy.copy(self.owner.global_rect.centerx)
        self.global_rect.centery = copy.copy(self.owner.global_rect.centery)

        hyp = (dx * dx + dy * dy) ** (1 / 2)
        try:
            self.sin = (dy / hyp)
        except ZeroDivisionError:
            self.sin = 0
        try:
            self.cos = (dx / hyp)
        except ZeroDivisionError:
            self.cos = 0

    def update(self, dt):
        super().update(dt)
        collide_list = collide_sprite(self, self.world.objects, has_sprite=True)

        for obj in collide_list:
            obj.on_collision(self)

        self.move_center(self.speed * self.cos * dt, self.speed * self.sin * dt)
        self.alive_time -= dt
        if self.alive_time <= 0:
            self.kill()

    def on_collision(self, obj):
        '''Со стреляющим не сталкиваемся'''
        if obj != self.owner:
            '''Не сталкиваемся с друзьями стреляющего'''
            if obj.team != self.owner.team and obj.team != 'world':
                obj.hp -= self.damage
                self.kill()

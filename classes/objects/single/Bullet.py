import copy

from classes.objects.single.Object import Object
import classes.gameconsts as config


class Bullet(Object):
    def __init__(self, owner, pos, world):
        super().__init__(0, 0, config.width_bullet, config.height_bullet, world)

        self.image = config.image_bullet
        self.rect = self.image.get_rect()

        self.speed = 1024 / 1000

        self.damage = 1

        self.owner = owner
        self.team = owner.team

        self.alive_time = 3000

        dx = copy.copy(pos[0]) - copy.copy(self.owner.rect.centerx)
        dy = copy.copy(pos[1]) - copy.copy(self.owner.rect.centery)

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

        self.move_center(self.speed * self.cos * dt, self.speed * self.sin * dt)
        self.alive_time -= dt
        if self.alive_time <= 0:
            self.kill()
            del self

    def on_collision(self, obj):
        """Со стреляющим не сталкиваемся"""
        if obj != self.owner:
            '''Не сталкиваемся с друзьями стреляющего'''
            if obj.team != self.owner.team and obj.team != 'world':
                obj.hp -= self.damage
                self.kill()
                del self

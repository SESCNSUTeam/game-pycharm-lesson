from classes.objects.single.Weapon import Weapon
from classes.objects.single.Object import Object
import classes.gameconsts as config


class Mob(Object):
    def __init__(self, x, y, world):

        super().__init__(x, y, config.width_mob, config.height_mob, world)

        self.image = config.image_mob
        self.rect = self.image.get_rect()
        self.team = 'mob'
        self.weight = 16 * 16

        self.acceleration = False
        self.speed = 256 / 1000

        self.weapon = Weapon(self)
        self.weapon.ammo = 60
        self.weapon.cool_down = 100
        self.weapon.curr_ammo = 100

        self.world = world

    def update(self, dt):
        super().update(dt)
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

    def calculate_action(self, **kwargs):
        target_pos = (kwargs['target'].rect.centerx, kwargs['target'].rect.centery)
        self.weapon.shoot(target_pos)

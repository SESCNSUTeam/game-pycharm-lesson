from classes.objects.net.server.ServerGameObject import ServerGameObject
import classes.gameconsts as config
from classes.objects.net.server.Weapon import Weapon


class Mob(ServerGameObject):

    class_id = 2

    def __init__(self, x, y, world):
        super().__init__(x, y, config.width_mob, config.height_mob, world)
        self.target = None
        self.has_target = False

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

        if not self.has_target:
            self.calculate_action()
        else:
            self.weapon.shoot((self.target.x, self.target.y))

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

    def calculate_action(self):
        for obj in self.world.objects:
            if obj.team == 'player':
                self.target = obj
                self.has_target = True

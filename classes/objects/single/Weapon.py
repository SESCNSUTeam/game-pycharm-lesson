from classes.objects.single.Bullet import Bullet


class Weapon:
    def __init__(self, owner):
        self.cool_down = 1000 / 30
        self.curr_cooldown = 0

        self.sps = 1000/self.cool_down

        self.ammo = 120
        self.curr_ammo = 0

        self.reload_time = 1000
        self.curr_reload_time = 0

        self.owner = owner

    def update(self, dt):
        if self.curr_cooldown >= 0:
            self.curr_cooldown -= dt

        if self.curr_reload_time >= 0:
            self.curr_reload_time -= dt
            if self.curr_reload_time <= 0:
                self.curr_ammo = self.ammo

    def shoot(self, pos):
        if self.curr_reload_time <= 0 and self.curr_cooldown <= 0:
            self.curr_ammo -= 1
            self.curr_cooldown = self.cool_down
            bullet = Bullet(self.owner, pos, self.owner.world)
            self.owner.world.objects.add(bullet)
            if self.curr_ammo <= 0:
                self.curr_reload_time = self.reload_time

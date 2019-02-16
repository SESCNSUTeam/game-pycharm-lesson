from math import sqrt


class Spell:
    def __init__(self,
                 wizard,
                 target,
                 spell_id,
                 timer=10000,   # time in millis
                 effect=None):
        self.spell_id = spell_id
        self.target = target
        self.wizard = wizard
        self.effect = effect
        self.timer = timer      # time in millis

    def update(self, dt):
        self.timer -= dt

    def draw(self, surface):
        # self.effect.draw(surface)
        pass

    def is_time_remaining(self):
        if self.timer <= 0:
            return False
        else:
            return True


class Throw(Spell):
    def __init__(self,
                 caster,
                 target):
        Spell.__init__(self, caster, target, 1, 1000)
        self.caster = caster
        self.target = target
        self.k = 1
        dx = target.centerx - caster.centerx
        dy = target.centery - caster.centery
        hyp = sqrt(dx**2 + dy**2)
        self.vx = (512/1000)*(dx/hyp)
        self.vy = (512/1000)*(dy/hyp)

    def update(self, dt):
        Spell.update(self, dt)
        self.k -= 0.001 * dt
        self.target.move(self.vx*dt*self.k, self.vy*dt*self.k)


class Grab(Spell):
    def __init(self,
               caster,
               target):
        Spell.__init__(self, caster, target, 2, 0)
        pass

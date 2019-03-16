class Effect:
    def __init__(self, caster):
        self.type = None
        self.inited = False
        self.caster = caster
        self.is_alive = True
        self.timer = 1000

    def init(self, *args):
        pass

    def update(self, **kwargs):
        pass

    def kill(self, buff_list=None):
        if buff_list is None:
            buff_list = []
        buff_list.remove(self)
        del self


class Force(Effect):
    def __init__(self, caster):
        super().__init__(caster)
        self.weight = caster.weight
        self.timer = 100
        self.distance = 0
        self.sin = None
        self.cos = None
        self.speed = 256/1000
        self.distance = 0

    def init(self, target):
        dx = (target.centerx - self.caster.centerx)
        dy = -(self.caster.centery - target.centery)
        try:
            self.cos = dx / (dy * dy + dx * dx) ** (1 / 2)
            self.sin = dy / (dy * dy + dx * dx) ** (1 / 2)
            self.distance = (dx * dx + dy * dy) ** (1 / 2)
        except ZeroDivisionError:
            self.is_alive = False

    def update(self, **kwargs):
        target = kwargs['target']
        dt = kwargs['dt']
        if self.sin == 0 and self.cos == 0:
            self.is_alive = False
        if not self.inited:
            self.init(target)
        if self.is_alive:
            force = self.weight/((self.distance**2)*target.weight)
            target.move_center(force * dt * self.cos/1000,
                               self.sin * dt * force/1000)
        self.timer -= dt
        if self.timer <= 0:
            self.is_alive = False


class Push(Effect):
    def __init__(self, caster):
        super().__init__(caster)
        self.type = 'directed'
        self.sin = None
        self.cos = None
        self.timer = 3000
        self.speed = 256 / 1000
        self.multi = 1

    def init(self, target):
        dx = (target.centerx - self.caster.centerx)
        dy = -(self.caster.centery - target.centery)
        try:
            self.cos = dx / (dy * dy + dx * dx) ** (1 / 2)
        except ZeroDivisionError:
            self.cos = 1
            
        try:
            self.sin = dy / (dy * dy + dx * dx) ** (1 / 2)
        except ZeroDivisionError:
            self.sin = 1

    def update(self, **kwargs):
        target = kwargs['target']
        dt = kwargs['dt']
        if self.sin == 0 and self.cos == 0:
            self.is_alive = False
        if not self.inited:
            self.init(target)
        if self.is_alive:
            target.move_center(self.speed * dt * self.cos * self.timer * self.multi / 1000,
                               self.sin * dt * self.speed * self.timer * self.multi / 1000)
            self.timer -= dt
            if self.timer <= 0:
                self.is_alive = False


class Pull(Effect):
    def __init__(self, caster):
        super().__init__(caster)
        self.type = 'directed'
        self.sin = None
        self.cos = None
        self.timer = 3000
        self.speed = 256 / 1000

    def init(self, target):
        dx = -(target.centerx - self.caster.centerx)
        dy = (self.caster.centery - target.centery)
        try:
            self.cos = dx / (dy * dy + dx * dx) ** (1 / 2)
            self.sin = dy / (dy * dy + dx * dx) ** (1 / 2)
        except ZeroDivisionError:
            self.is_alive = False

    def update(self, **kwargs):
        target = kwargs['target']
        dt = kwargs['dt']
        if self.sin == 0 and self.cos == 0:
            self.is_alive = False
        if not self.inited:
            self.init(target)
        if self.is_alive:
            target.move_center(self.speed * dt * self.cos * self.timer / 1000,
                               self.sin * dt * self.speed * self.timer / 1000)
            self.timer -= dt
            if self.timer <= 0:
                self.is_alive = False


class Hurt(Effect):
    def __init__(self, caster):
        super().__init__(caster)
        self.type = 'directed'
        self.timer = 1000
        self.dps = 10/1000

    def init(self, *args):
        # target = args[0]
        pass

    def update(self, **kwargs):
        target = kwargs['target']
        dt = kwargs['dt']

        if not self.inited:
            self.init(target)

        target.hp -= dt*self.dps

        if self.timer <= 0:
            self.is_alive = False


class Disable(Effect):
    def __init__(self, caster):
        super().__init__(caster)
        self.type = 'directed'
        self.timer = 3000

    def init(self, target):
        target.is_disable = True
        self.inited = False

    def update(self, **kwargs):
        dt = kwargs['dt']
        target = kwargs['dt']

        if not self.inited:
            self.init(target)

        self.timer -= dt
        if self.timer <= 0:
            target.is_disable = False
            self.is_alive = False


class Heal(Effect):
    def __init__(self, caster):
        super().__init__(caster)
        self.hps = 20/1000
        self.timer = 1000

    def update(self, **kwargs):
        target = kwargs['target']
        dt = kwargs['dt']
        target.hp += dt*self.hps
        self.timer -= dt
        if self.timer <= 0:
            self.is_alive = False


class Austral(Effect):
    def __init__(self, caster):
        super().__init__(caster)
        self.timer = 3000

    def init(self, target):
        target.is_collide = False
        self.inited = True

    def update(self, **kwargs):
        target = kwargs['target']
        dt = kwargs['dt']

        if not self.inited:
            self.init(target)

        self.timer -= dt
        if self.timer <= 0:
            target.is_collide = True
            self.is_alive = False

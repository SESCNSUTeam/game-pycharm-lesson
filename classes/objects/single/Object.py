from classes.objects.CommonGameObject import CommonGameObject


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
        self.is_collide = True
        self.effects = []
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

    def on_collision(self, obj):
        pass

    def is_alive(self):
        if self.hp <= 0:
            self.kill()
            del self

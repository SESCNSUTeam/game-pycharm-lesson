from classes.objects.single.Object import Object
import classes.gameconsts as config
from classes.magic.Effect import Push


class Brick(Object):
    def __init__(self, x, y, world):
        Object.__init__(self, x, y, config.width_brick, config.height_brick, world)
        self.image = config.image_brick
        self.rect = self.image.get_rect()
        self.weight = 48*16

    def update(self, dt):
        super().update(dt)

    def on_collision(self, obj):
        effect = Push(self)
        effect.timer = 100
        effect.multi = 30
        obj.buff([effect])

from classes.magic.Effect import Push
from classes.objects.net.server.ServerGameObject import ServerGameObject
import classes.gameconsts as config
import classes.idconfig as idconfig


class Brick(ServerGameObject):

    class_id = idconfig.id_brick

    def __init__(self, x, y, world):
        super().__init__(x, y, config.width_brick, config.height_brick, world)

    def update(self, dt):
        super().update(dt)

    def on_collision(self, obj):
        effect = Push(self)
        effect.timer = 100
        effect.multi = 30
        obj.buff([effect])

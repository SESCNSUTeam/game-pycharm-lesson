from classes.objects.net.server.ServerGameObject import ServerGameObject
import classes.gameconsts as config


class Mob(ServerGameObject):

    class_id = 1

    def __init__(self, x, y):
        super().__init__(x, y, config.width_mob, config.height_mob)
        self.speed = [1, 0]
        self.changed = False

    def update(self, dt):
        if self.left < 0:
            self.speed[0] = 1
        elif self.right > 600:
            self.speed[0] = -1
        self.move(self.speed[0], 0)
        self.changed = True

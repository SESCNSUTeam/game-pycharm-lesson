from classes.objects.net.client.ClientGameObject import ClientGameObject
import classes.gameconsts as config
import classes.idconfig as idconfig


class Brick(ClientGameObject):

    class_id = idconfig.id_brick

    def __init__(self, x, y):
        super().__init__(x, y, self.class_id)
        self.image = config.image_brick

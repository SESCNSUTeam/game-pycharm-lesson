from classes.objects.net.client.ClientGameObject import ClientGameObject
import classes.idconfig as idconfig


class Player(ClientGameObject):

    class_id = idconfig.id_player

    def __init__(self, x, y):
        super().__init__(x, y, self.class_id)
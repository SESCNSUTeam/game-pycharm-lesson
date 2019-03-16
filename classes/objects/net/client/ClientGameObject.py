from classes.gameconsts import image_dict
from classes.objects.CommonGameObject import CommonGameObject


class ClientGameObject(CommonGameObject):

    def __init__(self, x, y, class_id, obj_id):
        CommonGameObject.__init__(self, x, y)
        self.id = obj_id
        self.image = image_dict[class_id]
        self.rect = self.image.get_rect()
        self.global_rect.size = self.rect.size

    def set_pos(self, x, y):
        self.global_rect.x = x
        self.global_rect.y = y


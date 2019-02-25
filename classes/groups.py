from pygame.sprite import Group
from pygame import Rect
from classes.CommonGameObject import CommonGameObject


class ClientGroup(Group):

    def __init__(self):
        Group.__init__(self)
        self.id_dict = dict()

    def __setitem__(self, key, value):
        if key not in self.id_dict.items():
            self.id_dict[key] = value
            self.add(value)

    def __getitem__(self, key):
        return self.id_dict[key]

    def __delitem__(self, key):
        self.remove(self.id_dict[key])
        del self.id_dict[key]

    def __len__(self):
        return(len(self.sprites()))


"""

modifing


class CameraGroup(Group):

    def __init__(self, *sprites):
        Group.__init__(self, *sprites)
        self._target = CommonGameObject(self, 0, 0)

    @property
    def target(self):
        return self._target

    @target.setter
    def traget(self, value):
        self._target = value
        Group.add(self._targe
    def draw(self, surface):
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            rect = Rect(spr.x - self._target.x, spr.y - self._target.y, spr.rect.width, spr.rect.height)
            self.spritedict[spr] = surface_blit(spr.image, rect)
        self.lostsprites = []
"""
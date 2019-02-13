import pygame
from classes.CommonGameObject import CommonGameObject

""" не использовать эту камеру"""


class Camera(CommonGameObject):

    def __init__(self, x, y, w, h):
        CommonGameObject.__init__(self, x, y)
        self.region = pygame.Rect(0, 0, w, h)
        self.region.center = (x, y)
        self.background = pygame.sprite.RenderUpdates()
        self.objects = pygame.sprite.OrderedUpdates()

    def update_back(self, objects):
        for obj in objects:
            if self.region.contains(obj.rect) or self.region.colliderect(obj.rect):
                if obj not in self.background:
                    self.background.add(obj)
                obj.rect.move(self.region.left - obj.x, self.region.top - obj.y)
            else:
                if obj in self.background:
                    self.objects.remove(obj)

    def update_objects(self, objects):
        for obj in objects:
            if self.region.contains(obj.rect) or self.region.colliderect(obj.rect):
                if obj not in self.background:
                    self.objects.add(obj)
                new_x = obj.x - self.region.left
                new_y = obj.y - self.region.top
                obj.rect.move_ip(-obj.rect.left + new_x, -obj.rect.top + new_y)
            else:
                if obj in self.background:
                    self.objects.remove(obj)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.region.move_ip(dx, dy)

    def show(self, surface):
        self.background.draw(surface)
        self.objects.draw(surface)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + 680 / 2, -t + 720 / 2

    """
    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-680), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-720), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы
    """

    return pygame.Rect(l, t, w, h)


class Camera2:

    def __init__(self, width, height, camera_func=camera_configure):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)
        self.target = pygame.Rect(0, 0, 1, 1)

    def apply(self, targets):
        for target in targets:
            target.rect.move_ip(self.state.topleft)

    def update(self):
        self.state = self.camera_func(self.state, self.target)

    def move(self, dx, dy):
        self.target.move_ip(dx, dy)
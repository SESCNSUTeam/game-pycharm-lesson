from pygame.rect import Rect


class GameObject:
    def __init__(self, x, y, w, h, acceleration, speed=(0,0)):
        self.bounds = Rect(x, y, w, h)
        self.speed = speed
        self.acceleration = acceleration

    @property
    def left(self):
        return self.bounds.left

    @property
    def right(self):
        return self.bounds.right

    @property
    def top(self):
        return self.bounds.top

    @property
    def bottom(self):
        return self.bounds.bottom

    @property
    def width(self):
        return self.bounds.width

    @property
    def height(self):
        return self.bounds.height

    @property
    def center(self):
        return self.bounds.center

    @property
    def centerx(self):
        return self.bounds.centerx

    @property
    def centery(self):
        return self.bounds.centery

    def onCollision(self, object):
        pass

    def get_rect(self):
        return self.bounds

    def draw(self, surface):
        pass

    def move(self, dx, dy):
        self.bounds = self.bounds.move(dx, dy)

    def update(self,objects,dt):
        if self.speed == [0, 0]:
            return

        self.move(*self.speed)


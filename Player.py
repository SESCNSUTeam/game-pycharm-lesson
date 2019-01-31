from GameObject import GameObject
from Throw_Spell import Throw
import pygame
import config
class Player(GameObject):
    def __init__(self,x,y,image_dir,speed,acceleration, screen = None):
        self.image = pygame.image.load(image_dir)
        self.hp = 100
        GameObject.__init__(self,x,y,self.image.get_width(), self.image.get_height(), speed, acceleration)
        self._left = False
        self._right = False
        self._up = False
        self._down = False
        self._space = False
        self.c = False
        self.cast_list = []
    def handle(self,key):
        if key == pygame.K_a:
            self._left = not self._left
        if key == pygame.K_d:
            self._right = not self._right
        if key == pygame.K_s:
            self._down = not self._down
        if key == pygame.K_w:
            self._up = not self._up
        if key == pygame.K_SPACE:
            self._space = not self._space
        if key == pygame.K_c:
            self._c = not self._c
    def mouse_handle(self,pos):
        pass
    def update(self,dt):
        dx, dy = 0,0
        dax, day = 0,0
        if self._left:
            dx = -self.speed[0]*dt/1000
            dax = -self.acceleration[0]*((dt/1000)**2)
        if self._right:
            dx = self.speed[0]*dt/1000
            dax = self.acceleration[0] * ((dt / 1000) ** 2)
        if self._up:
            dy = -self.speed[1]*dt/1000
            day = -self.acceleration[1] * ((dt / 1000) ** 2)
        if self._down:
            dy = self.speed[1]*dt/1000
            day = self.acceleration[1] * ((dt / 1000) ** 2)
        if self._space:
            dx += dax
            dy += day

        # if self._c:
        #     self.cast_list.append(Throw())

        if(self.bounds.top + dy < 0):
            dy = 0
        if(self.bounds.bottom + dy > config.G_HEIGHT):
            dy = 0
        if(self.bounds.left + dx < 0):
            dx = 0
        if(self.bounds.right + dx > config.G_WIDTH):
            dx = 0
        if not self.isDisabled:
            self.move(dx,dy)

    def draw(self, surface):
        surface.blit(self.image,self.bounds)

    def onCollision(self,object):
        pass
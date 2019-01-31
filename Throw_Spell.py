from Spell import Spell
import pygame
class Throw(Spell):
    def __init__(self,wizard, point):
        self.point = point
        self.wizard = wizard
    def __init__(self,wizard, target):
        Spell.__init__(wizard, target)
        self.dps = 20/1000 #Damage in millis
        dx = wizard.centerx - target.centerx
        dy = wizard.centery - target.centery
        self.speed = (256*(dx/dy),256*(dy/dx))
        self.stop = False
        self.timer = 10000 #Time in millis
    def update(self, dt):
        self.timer -= dt
        if self.timer <= 0:
            self.stop = True
        self.target.hp -= self.dps*dt
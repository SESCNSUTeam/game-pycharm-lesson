from gamePycharmLesson.classes import CommonGameObject

import math
import pygame

from gamePycharmLesson.classes.GameObject import Wall, Player


class Monster(CommonGameObject):
    Id = 4
    type = "Monster"        #string value for getting type
    squadId = 0

    def __init__(self,start_x, start_y, w, h, vx, vy, hp, maxSpeed, attackPower):
        CommonGameObject.__init__(self, start_x, start_y, w, h)
        self.vx = vx
        self.vy = vy
        self.w = w
        self.h = h
        self.hp = hp
        self.maxSpeed = maxSpeed
        self.attackPower = attackPower

    def move(self):         #abstrackt methods
        pass

    def attack(self):       #
        pass

    def on_collision(self, obj):
        if isinstance(obj, Wall):
            wall = Wall(obj)

            rect = self.global_rect

            if rect.x + self.w <= wall.x and wall.y <= rect.y <= wall.y + wall.h:   #left collision case
                self.vx = -self.vx
            if rect.y <= wall.y + wall.h and wall.x <= rect.x <= wall.x + wall.w:   #down collision case
                self.vy = -self.vy
            if rect.x <= wall.x + wall.w and wall.y <= rect.y <= wall.y + wall.h:   #right collision case
                self.vx = -self.vx
            if rect.y + rect.h >= wall.y and  wall.x <= rect.x <= wall.x + wall.w:  #hight collision case
                self.vy = -self.vy
        if isinstance(obj, Player):
            return 1
        if isinstance(obj, Monster):
            pass

    def tactic(self):      #
        pass

    def update(self):
        pass

class Zombie(Monster):
    Id = 5
    def __init__(self,start_x, start_y):
        Monster.__init__(self, start_x, start_y, 3, 3, 10, 10, 5)

    def move(self, player):
        self.vx = get_vx(self.x, self.y, player.x, player.y, self.max_speed)
        self.vy = get_vy(self.x, self.y, player.x, player.y, self.max_speed)

    def attack(self, player):
        player.hp -= self.attackPower

    def tactic(self, playerList):
        pass
    def update(self):
        if self.hp <= 0:
            self = None
            return
        self.x += self.vx
        self.y += self.vy

def get_vx(x0, y0, x1, y1, speed):                  #moving to Player
    l = math.sqrt((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0))
    return int(speed*(x1-x0)/l)

def get_vy(x0, y0, x1, y1, speed):                  #
    l = math.sqrt((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0))
    return int(speed*(y1-y0)/l)

def makeSquade():       #this method maxes new monsters squads
    pass
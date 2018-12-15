import pygame as pg
import sys as system

class Activity:
    def __init__(self):
        self.width = 1280 # 16 : 9 monitor
        self.height = 720 #

        self.screen = pg.display.set_mode(width,height)


        pass

    def __new__(cls, *args, **kwargs):
        pg.init()


        pass
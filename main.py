import config as c
import pygame
from Mob import Mob
from Game import Game
class Main(Game):
    def __init__(self):
        Game.__init__(self,
                 "MAIN",
                 c.G_WIDTH,
                 c.G_HEIGHT,
                 "black.png",
                 c.G_FRAMERATE)

    def update(self,dt):
        for o in self.objects:
            o.update(self.objects,dt)


    def draw(self):
        for o in self.objects:
            o.draw(self.surface)





def main():
    mob = Mob(1,1,"brick.png",100,1)
    main = Main()
    main.objects.append(mob)
    main.run()

main()
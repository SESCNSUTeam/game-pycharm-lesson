import config as c
import pygame
from Player import Player
from Mob import Mob
from Game import Game

class Main(Game):
    def __init__(self,player):
        Game.__init__(self,
                 "MAIN",
                 c.G_WIDTH,
                 c.G_HEIGHT,
                 "black.png",
                 c.G_FRAMERATE)
        self.mobs = []
        self.player = player

    def update(self,dt):
        self.player.update(dt)
        for o in self.objects:
            o.update(dt)
        for m in self.mobs:
            m.update(dt,self.objects)

    def draw(self):
        self.player.draw(self.surface)
        for o in self.objects:
            o.draw(self.surface)
        for m in self.mobs:
            m.draw(self.surface)



def main():
    mob = Mob(1,1,"green.png",100,1)
    c = 64
    speed = (256,256)
    acceleration = (speed[0]*c,speed[1]*c)
    player = Player(1,1,"ball.png",speed,acceleration)

    main = Main(player)
    main.mobs.append(mob)

    main.keydown_handlers[pygame.K_w].append(player.handle)
    main.keydown_handlers[pygame.K_s].append(player.handle)
    main.keydown_handlers[pygame.K_a].append(player.handle)
    main.keydown_handlers[pygame.K_d].append(player.handle)
    main.keydown_handlers[pygame.K_SPACE].append(player.handle)
    main.keydown_handlers[pygame.K_c].append(player.handle)




    main.keyup_handlers[pygame.K_w].append(player.handle)
    main.keyup_handlers[pygame.K_s].append(player.handle)
    main.keyup_handlers[pygame.K_a].append(player.handle)
    main.keyup_handlers[pygame.K_d].append(player.handle)
    main.keyup_handlers[pygame.K_SPACE].append(player.handle)
    main.keyup_handlers[pygame.K_c].append(player.handle)

    main.run()

main()
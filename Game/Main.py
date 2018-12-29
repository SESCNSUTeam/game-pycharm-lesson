from Game import Game
from Runner import Runner
from Player import Player
from Mob import Mob
from Brick import Brick
from random import randint
import config as c
import pygame

def game():
    player = Player(130,130)

    screen = Game("My first caption",
                       1280,
                       720,
                       "ball.png",
                       60) #framerate
    #adding handle's methods
    screen.keydown_handlers[pygame.K_a].append(player.handle)
    screen.keydown_handlers[pygame.K_d].append(player.handle)
    screen.keydown_handlers[pygame.K_w].append(player.handle)
    screen.keydown_handlers[pygame.K_s].append(player.handle)

    screen.objects.append(player)

    screen.run()

def runer():
    player = Player(130, 130)

    screen = Runner("My first caption",
                       c.screen_width,
                       c.screen_height,
                       "ball.png",
                       c.frame_rate,
                    player)  # framerate
    # adding handle's methods
    screen.keydown_handlers[pygame.K_a].append(player.handle)
    screen.keydown_handlers[pygame.K_d].append(player.handle)
    screen.keydown_handlers[pygame.K_w].append(player.handle)
    screen.keydown_handlers[pygame.K_s].append(player.handle)
    screen.keyup_handlers[pygame.K_a].append(player.handle)
    screen.keyup_handlers[pygame.K_d].append(player.handle)
    screen.keyup_handlers[pygame.K_w].append(player.handle)
    screen.keyup_handlers[pygame.K_s].append(player.handle)

    screen.keydown_handlers[pygame.K_SPACE].append(player.handle)
    screen.keyup_handlers[pygame.K_SPACE].append(player.handle)
    screen.mouse_handlers.append(player.mouse_handle)
    # adding mobs and player
    for i in range(5):
        mob = Mob(randint(50, c.screen_width), randint(50, c.screen_height), 0)
        brick = Brick(randint(50, c.screen_width), randint(50, c.screen_height))
        screen.mobs.append(mob)
        screen.objects.append(brick)
    screen.run()

runer()
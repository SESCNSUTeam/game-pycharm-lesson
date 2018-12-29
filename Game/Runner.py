from Game import Game
from TextObject import TextObject
from Player import Player
from GameObject import GameObject
import sys
import pygame
import config as c
import Math

class Runner(Game):
    def __init__(self,
                 caption,
                 width,
                 height,
                 back_image_filename,
                 frame_rate,
                 player):
        Game.__init__(self, caption, width, height, back_image_filename, frame_rate)
        self.mobs = []
        self.player = player
        self.hp_bar = TextObject(30, 20,
                                 lambda: str(self.player.hp),
                                 (0, 0, 0),
                                 'Arial',
                                 20)
        self.show_message("Hello", (255,255,255), 'Arial', 20, True)


    def show_message(self,
                     text,
                     color = (255,255,255),
                     font_name='Arial',
                     font_size=20,
                     centralized=False):
        message = TextObject(c.screen_width // 2,
                             c.screen_height // 2,
                             lambda: text, color,
                             font_name, font_size)
        self.draw()
        message.draw(self.surface, centralized)
        pygame.display.update()
        pygame.time.wait(1000)

    def calculate_mob_moving(self, mob):
        dx = 0
        dy = 0

        mob.move(dx, dy)

    def calculate_mob_player_collision(self, mob):
        if mob.bounds.colliderect(self.player.bounds):
            self.player.hp -= mob.damage
            if self.player.hp <= 0:
                self.show_message("You dead",
                                  (155, 155, 0),
                                  'Arial', 30, True)
                self.game_over = True
            word1, word2 = Math.handle_collision_detect(mob, self.player)

    def update(self):
        self.player.update()
        for o in self.objects:
            o.update()

        for m in self.mobs:
            self.calculate_mob_moving(m)
            self.calculate_mob_player_collision(m)

    def draw(self):
        self.player.draw(self.surface)
        self.hp_bar.draw(self.surface, True)
        for o in self.objects:
            o.draw(self.surface)
        for m in self.mobs:
            m.draw(self.surface)

from classes.Event import convert_event_py_to_g, Click
from collections import defaultdict
from classes.Spell import *
import classes.config as c
import sys
import pygame

colour = 130, 30, 20


class SpellCaster:
    def __init__(self,
                 caption,
                 width,
                 height,
                 back_image_filename,
                 frame_rate,
                 player):
        self.player = player
        self.background_image = \
            pygame.image.load(back_image_filename)
        self.clock = pygame.time.Clock()
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        self.state = 'normal'
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []
        self.cast_list = []
        self.event_list = []
        self.objects.append(Player(600, 320, "..//resources//green.png"))  # Для теста

    def update(self, dt):
        for c in self.cast_list:
            c.update(dt)
            if not c.is_time_remaining():
                self.cast_list.remove(c)

        for o in self.objects:
            o.update(dt)

        self.player.update(dt)

    def draw(self):
        self.player.draw(self.surface)
        for o in self.objects:
            o.draw(self.surface)

    def run(self):
        while not self.game_over:
            self.surface.fill(colour)
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update(self.clock.get_time())
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)


def test():
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Hello")
    pygame.display.set_mode((1280, 720))

    while True:
        g_event_list = []
        py_event_list = pygame.event.get()
        for p_e in py_event_list:
            g_event_list.append(convert_event_py_to_g(p_e))

        for g_e in g_event_list:
            if g_e.type == c.MOUSEBUTTONDOWN:
                print(g_e.dict["pos"])
                click = Click(g_e.dict["pos"])
                g_event_list.append(click)
            if g_e.type == c.event_id_CLICK:
                print(g_e.dict["pos"])
        g_event_list.clear()
        py_event_list.clear()


def play():
    player = Player(5, 5, "..//resources//green.png")
    game = SpellCaster("Spell Caster", 1280, 720, "..//resources//black.png", 60, player)
    game.mouse_handlers.append(player.mouse_handle)
    game.keyup_handlers[pygame.K_a].append(player.handle)
    game.keyup_handlers[pygame.K_d].append(player.handle)
    game.keyup_handlers[pygame.K_s].append(player.handle)
    game.keyup_handlers[pygame.K_w].append(player.handle)
    game.keydown_handlers[pygame.K_a].append(player.handle)
    game.keydown_handlers[pygame.K_d].append(player.handle)
    game.keydown_handlers[pygame.K_s].append(player.handle)
    game.keydown_handlers[pygame.K_w].append(player.handle)
    game.run()


play()

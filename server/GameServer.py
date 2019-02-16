import pygame
from classes import MapLoader


class ServerGame:

    def __init__(self, tick):
        pygame.init()
        self.name = "Server"
        self.objects = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.shells = pygame.sprite.Group()
        self.tick = tick
        self.map = MapLoader.Map("maps/map_test.json")
        self.server = None
        self.clients = None
        self.pause = False
        self.play = True
        self.clock = pygame.time.Clock()

    def pre_init(self):
        pass

    def init(self):
        pass

    def post_init(self):
        pass

    def update(self, dt):
        pass

    def rifc(self):
        """receive info from clients"""
        pass

    def sitc(self, data):
        """send info to clients"""
        pass

    def form_data(self):
        pass

    def run(self):

        while self.play:
            self.rifc()
            if not self.pause:
                self.update(self.clock)
            data = self.form_data()
            self.sitc(data)

    def pause_server(self):
        self.pause = True

    def unpause_server(self):
        self.pause = False

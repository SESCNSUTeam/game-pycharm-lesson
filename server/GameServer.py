import pygame
from server.Server import Server
from classes.GameObject import SimpleMob
import sys


class GameServer:

    def __init__(self, host, port):
        pygame.init()
        self.server = Server(host, port)
        self.objects = pygame.sprite.Group()
        self.play = True

    @property
    def any_on_connect(self):
        return True if len(self.server.connections) else False

    def on_connect(self):
        pass

    def init(self):
        for i in range(30):
            obj = SimpleMob.instant(i, i * 20, 10, 10)
            self.objects.add(obj)

    def obj_info(self, act):
        info = []
        for obj in self.objects:
            obj_id, pos, cls_id = obj.info
            object_info = {"obj_id": obj_id, "act_id": act, "pos": pos, 'cls_id': cls_id}
            info.append(object_info)
        return info

    def run(self):
        self.server.start()
        self.init()
        c = pygame.time.Clock()
        while self.play:
            self.objects.update()
            if self.any_on_connect:
                inp = self.server.get_input()
                self.server.add_output_data([self.obj_info(1)])
            c.tick(300)


s = GameServer("localhost", 9060)
s.run()
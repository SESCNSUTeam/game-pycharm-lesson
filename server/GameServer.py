import pygame
from server.Server import Server
from classes.GameObject import SimpleMob


class GameServer:

    def __init__(self, host, port):
        pygame.init()
        self.server = Server(host, port)
        self.objects = pygame.sprite.Group()
        self.play = True

    def on_connect(self):
        pass

    def init(self):
        for i in range(4):
            obj = SimpleMob.instant(i, i * 20, 10, 10)
            self.objects.add(obj)

    def obj_init_info(self):
        init_info = []
        for obj in self.objects:
            obj_id, pos, cls_id = obj.info
            obj_info = {"obj_id": obj_id, "act_id": 0, "pos": pos, "cls_id": cls_id}
            init_info.append(obj_info)
        return init_info

    def obj_move_info(self):
        move_info = []
        for obj in self.objects:
            obj_id, pos, _ = obj.info
            obj_info = {"obj_id": obj_id, "act_id": 1, "pos": pos}
            move_info.append(obj_info)
        return move_info

    def run(self):
        self.server.start()
        self.init()
        c = pygame.time.Clock()
        while self.play:
            self.objects.update()
            if len(self.server.connections) != 0:
                inp = self.server.get_input()
                for cl_id in inp:
                    if inp[cl_id]:
                        for handl in inp[cl_id]:
                            if handl[1] == 0:
                                self.server.add_output_data(self.obj_init_info())
                            elif handl[1] == 1:
                                self.server.add_output_data(self.obj_move_info())
            c.tick(50)


s = GameServer("localhost", 9090)
s.run()
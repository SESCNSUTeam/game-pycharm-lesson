import copy
from collections import defaultdict

from classes.Camera import Camera
from classes.objects.net.client.ClientGameObject import ClientGameObject
from classes.images import *
from net.TCPConnection.TCPCientConnection import TCPClientConnection
from classes.groups import GameGroup
from classes.interface.menu import *

import classes.gameconsts as gameconsts

'''
Типы пакетов для приёма:
    0 - создать на клиенте [0, class_id, obj_id, (x, y, z)]
    1 - сдвинуть на клиенте [1, obj_id, (x, y)]
    2 - удалить на клиенте  [2, obj_id]

Типы пакетов для отправки:
    Одинаковые, структура: [id, action_id, *args]
'''


class Client:

    def __init__(self, size, fps, client_name):

        """ init block """
        pygame.init()
        pygame.font.init()
        pygame.joystick.init()
        """ display block """

        self.request_list = []

        self.resolution = size
        self.fps = fps
        self.icon = None
        self.caption = "Caster-Game"
        self.screen = pygame.display.set_mode(self.resolution, pygame.RESIZABLE)
        self.camera = Camera(self.resolution)

        self.camera_target = None
        self.is_camera_target = False

        self.name = client_name

        self.init()

        """ input block """

        # self.joys = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        # for j in self.joys:
        #     j.init()

        """ handlers block """

        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []
        self.event_list = []

        """ game const block """

        self.play = True
        self.output = []
        """ interface block """

        self.buttons = ButtonGroup()

        """ ingame block """

        self.objects = GameGroup()
        self.background = pygame.Surface(self.resolution)
        self.background.fill((254, 65, 43))
        self.session = None

    def init(self):
        '''Нужно для загрузки изображений'''
        gameconsts.image_player = load_image("..//..//resources//green.png")
        gameconsts.image_brick = load_image("..//..//resources//brick.png")
        gameconsts.image_mob = load_image("..//..//resources//red.png")
        gameconsts.image_bullet = load_image("..//..//resources//blue8x8.png")
        gameconsts.init()
        self.camera_target = ClientGameObject(0, 0, 3, -1)

    def set_caption(self, caption):
        self.caption = caption
        pygame.display.set_caption(self.caption)

    def set_icon(self, img):
        self.icon = img
        pygame.display.set_icon(img)

    def load_icon(self, icon):
        self.icon = pygame.image.load(icon)

    def set_resolution(self, resolution):
        self.resolution = resolution
        self.screen = pygame.display.set_mode(resolution)
        self.camera.set_size(resolution)

    def handler(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                cam_pos = (self.camera.global_rect.x, self.camera.global_rect.y)
                pos = (cam_pos[0] + event.pos[0], cam_pos[1] + event.pos[1])
                packet = [pygame.MOUSEMOTION, pos]
                self.output.append(packet)
            elif event.type in {pygame.KEYUP, pygame.KEYDOWN}:
                packet = [event.type, event.key]
                self.output.append(packet)
            elif event.type in {pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN}:
                packet = [event.type, event.button]
                self.output.append(packet)
            else:
                pass

    def update_display(self):
        self.screen.blit(self.background, (0, 0))
        self.camera.update(self.camera_target)
        self.camera.apply(self.objects)
        self.objects.draw(self.screen)
        self.buttons.draw(self.screen)
        pygame.display.flip()

    def connect_to_server(self, host, port):
        self.session = TCPClientConnection(host, port)
        self.session.connect()
        self.session.start()

    def create_object(self, packet):
        cl_obj = ClientGameObject(packet[3][0], packet[3][1], packet[1], packet[2])
        if (not self.is_camera_target) and (cl_obj.class_id == 3):
            self.camera_target = cl_obj
            self.is_camera_target = True
        self.objects[cl_obj.id] = cl_obj
        print('Object {} from packet {}'.format(object, packet))

    def move_object(self, packet):
        self.objects[packet[1]].x = packet[2][0]
        self.objects[packet[1]].y = packet[2][1]

    def remove_object(self, packet):
        del self.objects[packet[1]]
        print('deleted {}'.format(packet[1]))

    def send(self):
        """send information to server"""
        output = copy.copy(self.output)
        self.session.send(output)
        self.output.clear()
        self.request_list.clear()

    def receive(self):
        """receive information from server"""
        data = self.session.get_input()
        for packet in data:
            if packet[0] == 0:
                self.create_object(packet)
            elif packet[0] == 1:
                try:
                    self.move_object(packet)
                except KeyError:
                    request = ['request', packet[1]]
                    '''Проверка на то, что мы еще не отправляли этот запрос на данном тике'''
                    if packet[1] not in self.request_list:
                        self.request_list.append(packet[1])
                        print('request for {}'.format(packet[1]))
                        self.output.append(request)
            elif packet[0] == 2:
                try:
                    self.remove_object(packet)
                except KeyError:
                    print('Object with id {} doesn\'t exist'.format(packet[1]))

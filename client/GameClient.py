from collections import defaultdict
from classes import MapLoader
from classes.Event import convert_event_py_to_g
from classes.camera import Camera
from classes.GameObject import *
from client.Client import Client
from classes.groups import ClientGroup
from classes.interface.menu import *


class GameClient:

    def __init__(self, size, fps, client_name):

        """ init block """

        pygame.init()
        pygame.font.init()
        pygame.joystick.init()

        """ display block """

        self.resolution = size
        self.fps = fps
        self.icon = None
        self.caption = "Caster-Game"
        self.screen = pygame.display.set_mode(self.resolution, pygame.RESIZABLE)
        self.camera = Camera(self.resolution)
        self.name = client_name

        """ input block """

        self.joys = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        for j in self.joys:
            j.init()

        """ handlers block """

        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []
        self.event_list = []

        """ game const block """

        self.play = True

        """ interface block """

        self.buttons = ButtonGroup()

        """ ingame block """

        self.objects = ClientGroup()
        self.background = pygame.Surface(self.resolution)
        self.background.fill((254, 65, 43))
        self.map = MapLoader.Map("maps\map_test.json")
        self.session = None
        self.clock = pygame.time.Clock()

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

    def set_fps(self, fps):
        self.fps = fps

    def load_button(self, btn):
        self.buttons.add(btn)

    def quit(self):
        pygame.quit()
        sys.exit()

    def get_events(self):
        return pygame.event.get()

    def event_handling(self):
        for py_event in pygame.event.get():
            event = convert_event_py_to_g(py_event)
            self.event_list.append(event)
            if event.type == c.QUIT:
                self.play = False
                break
            elif event.type == c.KEYDOWN:
                for handler in self.keydown_handlers[event.dict["key"]]:
                    handler(event.dict["key"])
            elif event.type == c.KEYUP:
                for handler in self.keyup_handlers[event.dict["key"]]:
                    handler(event.dict["key"])
            elif event.type in (c.MOUSEBUTTONDOWN,
                                c.MOUSEBUTTONUP,
                                c.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.dict["pos"])
                self.buttons.handle(event.type, event.dict["pos"])
            elif event.type == c.RESIZE:
                self.set_resolution(event.dict["size"])
        self.event_list.clear()

    def update_display(self):
        self.screen.blit(self.background, (0, 0))
        self.camera.apply(self.objects)
        self.camera.apply(self.map.pr)
        self.map.pr.draw(self.screen)
        self.objects.draw(self.screen)
        self.buttons.draw(self.screen)
        pygame.display.flip()

    def connect_to_server(self, host, port):
        self.session = Client(host, port, self.name)
        self.session.conn()
        self.session.start()
        self.session.add_output_data([[], 0])
        data = self.session.get_input()
        while not data:
            data = self.session.get_input()
        return data

    def create_object(self, obj_info):
        cl_obj = ClientGameObject(obj_info['pos'][0], obj_info['pos'][1], obj_info['cls_id'])
        cl_obj.id = obj_info['obj_id']
        self.objects[cl_obj.id] = cl_obj

    def move_object(self, obj_info):
        obj_id, obj_pos = obj_info['obj_id'], obj_info['pos']
        self.objects[obj_id].x = obj_pos[0]
        self.objects[obj_id].y = obj_pos[1]

    def sits(self, msg):
        """send information to server"""
        self.session.add_output_data(msg)

    def rifs(self):
        """receive information from server"""
        data = self.session.get_input()
        return data[self.name]
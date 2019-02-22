from collections import defaultdict

from classes import MapLoader
from classes.Event import convert_event_py_to_g
from classes.camera import Camera
from classes.GameObject import *
from client.Client import Client


class GameClient:

    def __init__(self, size, fps):

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
        self.name = "client"

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

        """ ingame block """
        self.dict_objects = {}
        self.objects = pygame.sprite.Group()
        self.background = pygame.Surface(self.resolution)
        self.background.fill((254, 65, 43))
        self.map = MapLoader.Map("..//maps//map_test.json")
        self.session = None

        #self.camera_target = Player(40, 40)
        #self.objects.add(self.camera_target)
        #self.camera_target.set_controller(self)

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

    def load_objects(self, objects):
        for obj in objects:
            self.objects.add(obj)

    def load_object(self, obj):
        self.objects.add(obj)

    def has_object(self, obj):
        self.objects.has(obj)

    def quit(self):
        pygame.quit()
        sys.exit()

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
            elif event.type == c.RESIZE:
                self.set_resolution(event.dict["size"])
        self.event_list.clear()

    def update(self, dt):
        self.objects.update(dt)

    def update_display(self):
        self.screen.blit(self.background, (0, 0))
        self.camera.apply(self.objects)
        self.camera.apply(self.map.pr)
        self.map.pr.draw(self.screen)
        self.objects.draw(self.screen)
        pygame.display.flip()

    def connect_to_server(self, host, port):
        self.session = Client(host, port, self.name)
        self.session.conn()
        self.session.start()
        self.session.add_output_data([[[], 0]])
        data = self.session.get_input()
        print(data)
        return data

    def sits(self):
        """send information to server"""
        self.session.add_output_data([[[], 1]])

    def rifs(self):
        """receive information from server"""
        data = self.session.get_input()
        print(data)
        if data[self.name]:
            if data[self.name]:
                objects = data[self.name]
                for obj in objects:
                    if obj['act_id'] == 0:
                        cl_obj = ClientGameObject(obj['pos'][0], obj['pos'][1])
                        cl_obj.id = obj['obj_id']
                        self.objects.add(cl_obj)
                        self.dict_objects[cl_obj.id] = cl_obj
                    if obj['act_id'] == 1:
                        self.dict_objects[obj['obj_id']].x = obj['pos'][0]
                        self.dict_objects[obj['obj_id']].y = obj['pos'][1]

    def run(self):
        clock = pygame.time.Clock()
        data = self.connect_to_server("localhost", 9090)
        while self.play:
            self.sits()
            self.event_handling()
            self.rifs()
            self.update(clock.get_time())
            self.update_display()
            clock.tick(self.fps)
        self.quit()


ch = GameClient((600,  400), 50)
ch.run()

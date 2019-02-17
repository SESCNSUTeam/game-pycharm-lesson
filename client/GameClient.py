from collections import defaultdict

from classes import MapLoader
from classes.Event import convert_event_py_to_g
from classes.camera import Camera
from classes.GameObject import *


class GameClient:

    def __init__(self, size, fps):

        """ init block"""

        pygame.init()
        pygame.font.init()
        pygame.joystick.init()

        """ display block"""

        self.resolution = size
        self.fps = fps
        self.icon = None
        self.caption = "Caster-Game"
        self.screen = pygame.display.set_mode(self.resolution, pygame.RESIZABLE)
        self.camera = Camera(self.resolution)

        """ input block """

        self.joys = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        for j in self.joys:
            j.init()

        """ ingame block """

        self.objects = pygame.sprite.Group()
        self.background = pygame.Surface(self.resolution)
        self.background.fill((254, 65, 43))
        self.map = MapLoader.Map("maps\map_test.json")
        self.session = None

        self.camera_target = Player(40, 40)
        self.objects.add(self.camera_target)
        self.camera_target.set_controller(self)

        """ handlers block """

        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []
        self.event_list = []

        """ game const block """

        self.do_quit = False
        self.play = True

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

    def delete_object(self, obj):
        obj.do_kill()

    def has_object(self, obj):
        self.objects.has(obj)

    def quit(self):
        pygame.quit()
        sys.exit()

    def sits(self):
        """send information to server"""
        pass

    def rifs(self):
        """receive information from server"""
        pass

    def event_handling(self):
        for py_event in pygame.event.get():
            event = convert_event_py_to_g(py_event)
            self.event_list.append(event)
            if event.type == c.QUIT:
                self.do_quit = True
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
        self.camera_target.update(dt)
        self.camera.update(self.camera_target)
        self.objects.update(dt)

    def update_display(self):
        self.screen.blit(self.background, (0, 0))
        self.camera.apply(self.objects)
        self.camera.apply(self.map.pr)
        self.map.pr.draw(self.screen)
        self.objects.draw(self.screen)
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while self.play:
            self.sits()
            self.event_handling()
            self.rifs()
            if self.do_quit:
                self.quit()
            self.update(clock.get_time())
            self.update_display()
            clock.tick(self.fps)


client = GameClient((1280, 720), 60)
client.run()

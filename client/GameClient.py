import sys

import pygame

from classes.Event import convert_event_py_to_g
from classes.Camera import Camera2
from classes.GameObject import ClientGameObject
import classes.config as c

#imported by Bulat
from collections import defaultdict


class GameClient:

    def __init__(self, size, fps):
        pygame.init()
        pygame.font.init()
        self.width = size[0]
        self.height = size[1]
        self.fps = fps
        self.background = pygame.Surface(self.size())
        self.background.fill((254, 65, 43))
        self.objects = pygame.sprite.Group()
        self.icon = None
        self.caption = None
        self.play = True
        self.client = None
        self.server = None
        self.events = None
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.camera = Camera2(self.width, self.height)
        self.camera.move(10, 0)

        # new fields which added by Bulat
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.cast_list = []
        self.event_list = []
        self.mouse_handlers = []

    def set_caption(self, caption):
        self.caption = caption
        pygame.display.set_caption(self.caption)

    def set_icon(self, img):
        self.icon = img
        pygame.display.set_icon(img)

    def size(self):
        return self.width, self.height

    def load_icon(self, icon):
        self.icon = pygame.image.load(icon)

    def set_resolution(self, resolution):
        self.width = resolution[0]
        self.height = resolution[1]

    def set_fps(self, fps):
        self.fps = fps

    def load_objects(self, objects):
        for obj in objects:
            self.objects.add(obj)

    def load_object(self, obj):
        self.objects.add(obj)

    def delete_object(self, obj):
        self.objects.remove(obj)

    def has_object(self, obj):
        self.objects.has(obj)

    def sits(self):
        """send information to server"""
        pass

    def rifs(self):
        """receive information from server"""
        pass

    def event_handling(self):
        for py_event in pygame.event.get():
            self.event_list.append(convert_event_py_to_g(py_event))

        for event in self.event_list:
            if event.type == c.QUIT:
                pygame.quit()
                sys.exit()
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
        self.event_list.clear()

    def update(self):
        self.camera.update()
        pass

    def spell_handling(self, event):
        pass

    def update_display(self):
        self.screen.blit(self.background, (0, 0))
        self.camera.apply(self.objects)
        self.objects.draw(self.screen)
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while self.play:
            self.event_handling()
            self.update()
            self.update_display()
            clock.tick(self.fps)


client = GameClient((680, 720), 60)
dog = ClientGameObject(0, 0, "resources//dog.jpg")
client.load_object(dog)
client.run()

import pygame
from time import time, sleep
from myGame.GameObject import CommonGameObject


class GameClient:

    def __init__(self, size, fps):
        pygame.init()
        self.width = size[0]
        self.height = size[1]
        self.fps = fps
        self.objects = pygame.sprite.RenderPlain()
        self.icon = None
        self.caption = None
        self.background = pygame.Surface(self.size())
        self.play = True
        self.time_per_frame = 0
        self.client = None
        self.server = None
        self.events = None
        self.screen = pygame.display.set_mode((self.width, self.height))

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
        if pygame.display.get_active():
            for event in pygame.event:
                
    def update_display(self):
        pass

    def run(self):
        clock = pygame.time.Clock()
        while self.play:
            clock.tick(60)

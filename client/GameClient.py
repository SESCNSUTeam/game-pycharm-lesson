
import pygame
from classes.camera import Camera2
from classes.GameObjects import ClientGameObject


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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False
                if event.type == pygame.KEYDOWN:
                    pass
                    """
                    if event.key == pygame.K_d:
                        self.her.move(10, 0)
                    elif event.key == pygame.K_a:
                        self.her.move(-10, 0)
                    elif event.key == pygame.K_w:
                        self.her.move(0, 10)
                    elif event.key == pygame.K_s:
                        self.her.move(0, -10)
                    """
    def update(self):
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
            print(self.camera.state.left)


client = GameClient((680, 720), 60)
dog = ClientGameObject(0, 0, "resources\\dog.jpg")
client.load_object(dog)
client.run()
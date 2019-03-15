import pygame
from collections import defaultdict

import classes.config as config
from classes.GameObject import load_image
from classes.camera import Camera
from demo.objects import Player, Brick


class Game:
    def __init__(self, resolution, ):
        self.resolution = resolution
        self.background = pygame.Surface(self.resolution)
        self.background.fill((254, 65, 43))

        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        self.init()

        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []
        self.camera = Camera(self.resolution)
        self.objects = pygame.sprite.Group()

        self.player = Player(50, 50)
        self.camera_target = self.player
        self.player.set_controller(self.keydown_handlers, self.keyup_handlers, self.mouse_handlers)
        self.objects.add(self.player)

        self.action_list = []

        for i in range(10):
            brick = Brick(32 + config.brick_width * i * 2, 360)
            self.objects.add(brick)

    def init(self):
        config.player_image = load_image("..//resources//green.png")
        config.player_width = 32
        config.player_height = 32

        config.brick_image = load_image("..//resources//brick.png")
        config.brick_width = 64
        config.brick_height = 32

    def handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)
            elif event.type in {pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP}:
                for handler in self.mouse_handlers:
                    handler(event.pos, event.button)
            elif event.type == pygame.MOUSEMOTION:
                pass
            elif event.type == pygame.USEREVENT + 1:
                event.spell.cast_spell(self, event.pos)
            elif event.type == pygame.USEREVENT + 2:
                event.scroll.use_scroll(self, event.pos)

    def update(self, dt):
        # for action in self.action_list:
        #     if not action.is_alive:
        #         action.kill(self.action_list)
        #         continue
        #     action.update(dt)

        for o in self.objects:
            if o.is_disabled:
                continue
            o.update(dt)
            collide_objects = pygame.sprite.spritecollide(o, self.objects, dokill=False)
            for obj in collide_objects:
                obj.on_collision(o)
                o.on_collision(obj)

        self.camera.update(self.player)

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.camera.apply(self.objects)
        self.objects.draw(self.screen)
        pygame.display.flip()

    def start(self):
        clock = pygame.time.Clock()
        while True:
            self.handler()
            self.update(clock.get_time())
            self.render()
            clock.tick(60)


game = Game((1280, 720))
game.start()
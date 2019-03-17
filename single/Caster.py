from collections import defaultdict

import pygame
import classes.gameconsts as config
from classes.Camera import Camera
from classes.images import load_image
from classes.objects.single.Brick import Brick
from classes.objects.single.Mob import Mob
from classes.objects.single.Player import Player


def collide_sprite(sprite, sprite_group, has_sprite=True):
    collide_list = []

    for s in sprite_group:
        if has_sprite:
            if s == sprite:
                has_sprite = False
                continue

        if sprite.rect.colliderect(s.rect):
            collide_list.append(s)

    return collide_list


class Caster:

    def __init__(self, resolution):
        '''Настройка pygame дисплея'''
        self.resolution = resolution
        self.background = pygame.Surface(self.resolution)
        self.background.fill((254, 65, 43))

        pygame.init()

        self.screen = pygame.display.set_mode(self.resolution, pygame.FULLSCREEN)
        self.init()
        '''Список хендлеров'''
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []
        '''Камера и объекты'''
        self.camera = Camera(self.resolution)
        self.objects = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        '''Создание игрока'''
        self.player = Player(80, 120, self)
        self.player.set_controller(self.keydown_handlers, self.keyup_handlers, self.mouse_handlers)
        self.objects.add(self.player)

        '''Мировые эффекты и события'''
        self.action_list = []
        '''Добавляю тест-объекты'''
        for i in range(2):
            brick = Brick(32 + config.width_brick * i * 2, 360, self)
            self.objects.add(brick)
            mob = Mob(32, 180 + config.width_mob * i * 2, self)
            self.objects.add(mob)
            self.mobs.add(mob)

        self.camera.apply(self.objects)

    def init(self):
        '''Нужно для загрузки изображений'''
        config.image_player = load_image("..//resources//green.png")
        config.image_brick = load_image("..//resources//brick.png")
        config.image_mob = load_image("..//resources//red.png")
        config.image_bullet = load_image("..//resources//blue8x8.png")

    def handler(self):
        '''Просто хендлер, внутренняя логика игры'''
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
            elif event.type == config.event_spell:
                event.spell.cast_spell(self, event.pos)
            elif event.type == config.event_scroll:
                event.scroll.use_scroll(self, event.pos)
            elif event.type == config.event_calculate_behavior:
                pass

    def update(self, dt):
        for action in self.action_list:
            if not action.is_alive:
                action.kill(self.action_list)
                continue
            action.update(dt)

        for o in self.objects:
            collide_objects = collide_sprite(o, self.objects)
            for obj in collide_objects:
                obj.on_collision(o)

        for m in self.mobs:
            m.calculate_action(target=self.player)

        for o in self.objects:
            o.update(dt)

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
            print(1000 / clock.get_time())


game = Caster((1920, 1080))
game.start()

from classes.CommonGameObject import CommonGameObject

import pygame


class TextObject(CommonGameObject):
    def __init__(self, pos, text_func, color, font_name, font_size):
        CommonGameObject.__init__(self, pos[0], pos[1])
        self.text_func = text_func
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.bounds = self.get_surface(text_func())

    def draw(self, surface, centralized=False):
        text_surface, self.bounds = \
            self.get_surface(self.text_func())
        if centralized:
            pos = (self.x - self.bounds.width // 2,
                   self.y)
        else:
            pos = (self.x, self.y)
        surface.blit(text_surface, pos)

    def get_surface(self, text):
        text_surface = self.font.render(text,
                                        False,
                                        self.color)
        return text_surface, text_surface.get_rect()


class Button(CommonGameObject):

    def __init__(self, size, pos, press_func):
        CommonGameObject.__init__(self, pos[0], pos[1])
        self.size = size
        self.text_object = None
        self.press_func = press_func
        self.image = None

    def set_size(self, size):
        self.size = size

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def load_text(self, pad_x, pad_y, text, color, font, font_size):
        pos = self.x + pad_x, self.y + pad_y
        self.text_object = TextObject(pos, text, color, font, font_size)

    def check_mouse_on(self, mouse_pos):
        return mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.size[0] and mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.size[1]

    def on_pressed(self, *args):
        self.press_func(args)

    def set_img(self, img):
        self.image = img
        self.rect = pygame.Rect()

import pygame
import classes.config as config


AL_CENTER = 'c'
AL_LEFT = 'l'
AL_RIGHT = 'r'
AL_TOP = 't'
AL_DOWN = 'd'

deft = lambda x: 0


class TextObject:

    def __init__(self, text, color, font, align=AL_CENTER):
        self.text = text
        self.color = color
        self.font = font
        self.align = align

    def get_surface(self):
        text_surface = self.font.render(self.text, False, self.color)
        return text_surface

    def change_text(self, text):
        if isinstance(text, str):
            self.text = text
        else:
            raise TypeError


class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h, text_obj, b_color, on_down=deft, on_up=deft, on_mouse=deft):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text_obj
        self.on_down = on_down
        self.on_up = on_up
        self.on_motion = on_mouse
        self.color = b_color
        self.image = self.render(self.text)

    def on_pressed(self, pos, *args, **kwargs):
        if self.rect.collidepoint(pos[0], pos[1]):
            return self.on_down(*args, **kwargs)

    def on_unpressed(self, pos, *args, **kwargs):
        if self.rect.collidepoint(pos[0], pos[1]):
            return self.on_up(pos, *args, **kwargs)

    def on_mouse_motion(self, pos, *args, **kwargs):
        if self.rect.collidepoint(pos[0], pos[1]):
            return self.on_motion(pos, *args, **kwargs)

    def set_functions(self, on_down, on_up, on_motion):
        self.on_down = on_down
        self.on_up = on_up
        self.on_motion = on_motion

    def render(self, text):
        sub_surf = pygame.Surface((self.rect.w, self.rect.h))
        text_surf = text.get_surface()
        text_rect = text_surf.get_rect()

        if text.align == AL_CENTER:
            left = (self.rect.w - text_rect.w)/2
            top = (self.rect.h - text_rect.h)/2
        else:
            left, top = 0, 0
        sub_surf.blit(text.get_surface(), (left, top))
        return sub_surf

    def change_text(self, text):
        self.text.change_text(text)


def gameButton(x, y, w, h, b_color, text, t_size, font_name, t_color,
               align=AL_CENTER, on_down=deft, on_up=deft, on_mouse=deft):
    font = pygame.font.SysFont(font_name, t_size)
    textobj = TextObject(text, t_color, font, align)
    button = Button(x, y, w, h, textobj, b_color, on_down, on_up, on_mouse)
    return button


class ButtonGroup(pygame.sprite.Group):

    def __init__(self, *buttons):
        pygame.sprite.Group.__init__(self, *buttons)
        self.buttons_events = []

    def on_pressed(self, pos, *args, **kwargs):
        for btn in self.sprites():
            self.buttons_events.append(btn.on_pressed(pos, *args, **kwargs))

    def on_unpressed(self, pos, *args, **kwargs):
        for btn in self.sprites():
            self.buttons_events.append(btn.on_unpressed(pos, *args, **kwargs))

    def on_mouse_motion(self, pos, *args, **kwargs):
        for btn in self.sprites():
            self.buttons_events.append(btn.on_mouse_motion(pos, *args, **kwargs))

    def handle(self, ev_type, pos, *args, **kwargs):
        if ev_type == config.MOUSEBUTTONDOWN:
            self.on_pressed(pos, *args, **kwargs)
        elif ev_type == config.MOUSEBUTTONUP:
            self.on_unpressed(pos, *args, **kwargs)
        elif ev_type == config.MOUSEMOTION:
            self.on_mouse_motion(pos, *args, **kwargs)

    def get_button_events(self):
        bev = self.buttons_events
        self.buttons_events = []
        return bev

    """
class InputBox:

    def __init__(self, x, y, w, h, text_color, button_text, text_size):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = ''
        self.txt_surface = pygame.font.Font(None, text_size).render(self.text, True, self.color)
        self.active = False
        self.

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(*event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
    """
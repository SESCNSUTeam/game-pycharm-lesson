from classes.interface.button import *
from classes.interface.iconfig import *


def default(*args):
    return 0


def simlpeButton(x, y, w, h, text, size, on_down=default, on_up=default, on_motion=default):
    gb = gameButton(x, y, w, h, white, text, size, pygame.font.get_default_font(),
               black, AL_CENTER, on_down, on_up, on_motion)
    return gb


def rectButton(x, y, r, text, size, on_down=default, on_up=default, on_motion=default):
    gb = gameButton(x, y, r, r, white, text, size, pygame.font.get_default_font(),
                    black, AL_CENTER, on_down, on_up, on_motion)
    return gb


def build_stock_interface(button_number, screen_size):

    w = int(screen_size[0]/3)
    h = int(screen_size[1]/3)

    left = int(screen_size[0] - w) / 2
    top = int(screen_size[1] - h) / 2

    step = 5

    bh = int(h / button_number) - step
    bw = w

    text_size = 32

    button_list = []

    for i in range(button_number):
        x = left
        y = (bh+step)*i + top
        btm = simlpeButton(x, y, bw, bh, '', text_size)
        button_list.append(btm)

    return button_list

import pygame as pg
import


def convert_event_g_to_py(g_event):
    e = pg.event.Event(c.USEREVENT + g_event.type, g_event.dict)
    return e


def convert_event_py_to_g(pygame_event):

    def fill_dict(py_event, dictionary):
        if py_event.type == pg.KEYDOWN:
            dictionary["key"] = py_event.key
        elif py_event.type == pg.KEYUP:
            dictionary["key"] = py_event.key
        elif py_event.type in (pg.MOUSEBUTTONDOWN,
                               pg.MOUSEBUTTONUP,
                               pg.MOUSEMOTION):
            dictionary["pos"] = py_event.pos
        elif py_event.type in c.SPELLIDRANGE:
            dictionary["caster"] = py_event.caster
            dictionary["target"] = py_event.target
            dictionary["spell"] = py_event.spell

    d = dict()
    g_event = GEvent(pygame_event.type - c.USEREVENT, d)
    fill_dict(pygame_event, d)

    return g_event


class GEvent:

    def __init__(self, type, dict):
        self.type = type
        self.dict = dict

    def post(self):
        e = convert_event_g_to_py(self)
        pg.event.post(e)


class Cast(GEvent):

    def __init__(self,type, dict):
        GEvent.__init__(self,type, dict)

    def post(self):
        GEvent.post(self)
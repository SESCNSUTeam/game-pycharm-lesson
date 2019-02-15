import pygame as pg
import classes.config as c


def convert_event_g_to_py(g_event):
    e = pg.event.Event(c.user_event + g_event.type, g_event.dict)
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
        elif py_event.type == c.event_id_EXIST + c.user_event:  # exist event
            dictionary["exist"] = True
        elif py_event.type == c.event_id_CLICK + c.user_event:  # click event
            # Здесь будем проверять последовательность действий клика: заклинания, к примеру
            # Прим.: act_list[0] == "spell" => по значению act_list[1] узнаем заклинание
            # Прим.: act_list[0] == "attack" => у act_list не будет больше значение, но, к примеру,
            # по точке будем смотреть на наличие противника и т.д.
            if py_event.send:
                dictionary["send"] = True
                dictionary["pos"] = py_event.pos
                dictionary["entity"] = py_event.entity
                dictionary["act_list"] = py_event.act_list
        elif py_event.type == c.event_id_MOVE + c.user_event:   # move event
            dictionary["entity"] = py_event.entity
            dictionary["turn"] = py_event.turn
        elif py_event.type == c.event_id_SPAWN + c.user_event:  # spawn event
            dictionary["entity"] = py_event.entity
            dictionary["pos"] = py_event.pos
        elif py_event.type == c.event_id_SPELL + c.user_event:  # cast event
            dictionary["caster"] = py_event.caster_id
            dictionary["target"] = py_event.target_id
            dictionary["spell"] = py_event.spell_id
        elif py_event.type == pg.VIDEORESIZE:
            dictionary["size"] = (py_event.w, py_event.h)
        else:
            dictionary["not_defined"] = True
    d = dict()
    fill_dict(pygame_event, d)
    g_event = Event(pygame_event.type - c.user_event, d)
    return g_event


class Event:
    def __init__(self, type, dict):
        self.type = type
        self.dict = dict

    def post(self):
        e = convert_event_g_to_py(self)
        pg.event.post(e)


class Cast(Event):
    def __init__(self, dict):
        Event.__init__(self, c.spell_event_id, dict)  # includes wizard, target and spell_id (GameObject, GameObject, int)

    def post(self):
        Event.post(self)


class Exist(Event):
    def __init__(self):
        Event.__init__(self, c.event_id_EXIST, {"isExist": True})    # sending accept that player didn't disconnect

    def post(self):
        Event.post(self)


class Spawn(Event):                                                    # spawn entity on
    def __init__(self, entity, pos):
        Event.__init__(c.event_id_SPAWN, {"pos": pos, "entity": entity})

    def post(self):
        Event.post(self)


class Move(Event):
    def __init__(self, entity, turn):
        Event.__init__(self, c.event_id_MOVE, {"turn": turn, "entity": entity})

    def post(self):
        Event.post(self)


class Click(Event):
    def __init__(self, pos, entity, act_list=[], send=True):
        Event.__init__(self, c.MOUSECLICK, {"pos": pos, "entity": entity, "act_list": act_list, "send": send})

    def post(self):
        Event.post(self)
#
#
# class KeyPressed(Event):
#     def __init__(self, key):
#         Event.__init__(self, c.event_id_KEYPRESSED, {"key": key})
#
#     def post(self):
#         Event.post(self)


class Resize(Event):
    def __init__(self, size=(0, 0)):
        Event.__init__(self, c.RESIZE)

    def post(self):
        Event.post(self)

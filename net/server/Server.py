import copy

import pygame
from collections import defaultdict

from classes.groups import GameGroup
from classes.objects.net.server.Brick import Brick
from classes.objects.net.server.Player import Player
from net.TCPConnection.TCPServerConnection import TCPServerConnection
import classes.gameconsts as gameconsts

'''
Типы пакетов для отправки:
    0 - создать на клиенте [0, class_id, obj_id, (x, y, z)]
    1 - сдвинуть на клиенте [1, obj_id, (x ,y, z)]
    2 - удалить на клиенте  [2, obj_id]

Типы пакетов для приёма:
    Одинаковые, структура: [id_connection, [action_id, *args]]
    или [id_connection, [ request, obj_id]]
'''


def get_handlers():
    return defaultdict(list), defaultdict(list), []


class Server:
    def __init__(self, host, port):
        self.server = TCPServerConnection(host, port, 4, self)
        pygame.init()
        self.packets = []

        self.player_handlers = dict()

        self.play = True

        self.objects = GameGroup()
        self.mobs = pygame.sprite.Group()

        self.player_dict = dict()

        self.team = 'player'

        for i in range(15):
            brick = Brick((gameconsts.width_brick + 5) * i, 32, self)
            self.objects[brick.id] = brick

    def on_connection(self, conn_number, conn=None):
        print('Connected {} {}'.format(conn_number, conn))
        player = Player(30, 30, self)
        self.player_dict[conn_number] = player

        down, up, mouse = get_handlers()
        player.set_controller(down, up, mouse)
        player.team = copy.copy(self.team)
        self.team += '1'
        self.player_handlers[conn_number] = [down, up, mouse]
        self.objects[player.id] = player
        print('Conn number is {}'.format(conn_number))
        packet = [0, player.class_id, player.id, (player.x, player.y, 0)]
        self.server.push_data(packet)
        for obj in self.objects:
            if obj == player:
                continue
            packet = [0, copy.copy(obj.class_id), copy.copy(obj.id), (copy.copy(obj.x), copy.copy(obj.y), 0)]
            self.server.push_data_by_number(packet, conn_number)
        # print('All information has been sent to {}'.format(conn))

    def on_disconnect(self, conn_number, conn=None):
        print('Disconnected: {}'.format(conn))
        player = self.player_dict[conn_number]
        packet = [2, copy.copy(player.id)]
        self.server.push_data(packet)
        player.kill()
        del self.player_dict[conn_number]
        del player

    def handler(self):
        for packet in self.packets:
            conn_id = packet[0]
            event = packet[1]
            if event[0] == pygame.MOUSEMOTION:
                self.player_dict[conn_id].mouse_pos = event[1]
            elif event[0] == pygame.KEYUP:
                for handler in self.player_handlers[conn_id][1][event[1]]:
                    handler(event[1], False)
            elif event[0] == pygame.KEYDOWN:
                for handler in self.player_handlers[conn_id][0][event[1]]:
                    handler(event[1], True)
            elif event[0] == pygame.MOUSEBUTTONUP:
                for handler in self.player_handlers[conn_id][2]:
                    handler(event[1], False)
            elif event[0] ==  pygame.MOUSEBUTTONDOWN:
                for handler in self.player_handlers[conn_id][2]:
                    handler(event[1], True)

        for event in pygame.event.get():
            if event.type == gameconsts.event_remove:
                try:
                    del self.objects[event.id]
                except KeyError:
                    print("Couldn't delete {}, doesn't exist".format(event.id))
                packet = [2, event.id]
                self.server.push_data(packet)
            elif event.type == gameconsts.event_spell:
                event.spell.cast_spell(self, event.pos)

        self.packets.clear()

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)

    def receive(self):
        input = self.server.get_input()
        for inp in input:
            conn_id = inp[0]
            packet = inp[1]
            if packet[0] == 'request':
                try:
                    obj = self.objects[packet[1]]
                    packet = [0, obj.class_id, obj.id, (obj.x, obj.y, 0)]
                    self.server.push_data_by_number(packet, conn_id)
                except KeyError:
                    print('Error, obj with id {} has not been founded')
                    print('Info about packet: connection_number {}, packet {}'.format(inp[0], inp[1]))
            else:
                self.packets.append(inp)

    def send(self):
        for obj in self.objects:
            packet = [1, copy.copy(obj.id), (copy.copy(obj.x), copy.copy(obj.y), 0)]
            self.server.push_data(packet)

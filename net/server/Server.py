import copy

import pygame
from collections import defaultdict

from classes.groups import GameGroup
from classes.objects.net.server.Brick import Brick
from classes.objects.net.server.Player import Player
from net.TCPConnection.TCPServerConnection import TCPServerConnection
import classes.gameconsts as config

'''
Типы пакетов для отправки:
    0 - создать на клиенте [0, class_id, obj_id, (x, y, z)]
    1 - сдвинуть на клиенте [1, obj_id, (x ,y, z)]
    2 - удалить на клиенте  [2, obj_id]

Типы пакетов для приёма:
    Одинаковые, структура: [id_connection, [action_id, *args]]
    или [id_connection, [ request, obj_id]]
'''


class Server:
    def __init__(self, host, port):
        self.server = TCPServerConnection(host, port, 4, self)

        self.packets = []
        self.mouse_handlers = []
        self.key_down_handlers = defaultdict(list)
        self.key_up_handlers = defaultdict(list)

        self.play = True

        self.objects = GameGroup()
        self.mobs = pygame.sprite.Group()

        self.player_dict = dict()

        for i in range(2):
            brick = Brick(32 + config.width_brick * 2 * i, 32, self)
            self.objects[brick.id] = brick

    def on_connection(self, conn_number, conn=None):
        print('Connected {} {}'.format(conn_number, conn))
        player = Player(30, 30, self)
        self.player_dict[conn_number] = player
        player.set_controller(self.key_down_handlers, self.key_up_handlers, self.mouse_handlers)
        self.objects[player.id] = player
        packet = [0, player.class_id, player.id, (player.x, player.y, 0)]
        self.server.push_data(packet)
        for obj in self.objects:
            if obj == player:
                continue
            packet = [0, copy.copy(obj.class_id), copy.copy(obj.id), (copy.copy(obj.x), copy.copy(obj.y), 0)]
            self.server.push_data_by_number(packet, conn_number)
        print('All information has been sent to {}'.format(conn))

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
                print('Key pushed!')
                for handler in self.key_up_handlers[event[1]]:
                    handler(event[1])
            elif event[0] == pygame.KEYDOWN:
                print('Key unpushed!')
                for handler in self.key_down_handlers[event[1]]:
                    handler(event[1])
            elif event[0] in {pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN}:
                pass

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
                    print('Error, obj with id {} has not been founded'.format(inp[2]))
                    print('Info about packet: connection_number {}, packet {}'.format(inp[0], inp[1]))
            else:
                self.packets.append(inp)

    def send(self):
        for obj in self.objects:
            packet = [1, obj.id, (obj.x, obj.y, 0)]
            self.server.push_data(packet)

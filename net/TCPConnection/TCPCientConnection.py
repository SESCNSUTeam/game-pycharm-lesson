import copy
import pygame
import socket
import pickle
import threading
import select

from time import sleep


class TCPClientConnection(threading.Thread):
    def __init__(self, host, port):
        super().__init__(target=self.run)
        self.address = (host, port)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = False
        self.name = -1
        self.lock = threading.Lock()
        self.output_queue = []
        self.input_queue = []

    def connect(self):
        try:
            self.socket.connect(self.address)
            self.socket.setblocking(False)
            return False
        except OSError:
            return True

    def handle_input(self, readable):
        for sock in readable:
            data = None
            try:
                data = sock.recv(2048)
                if data:
                    loaded_data = pickle.loads(data)
                    self.input_queue.append(loaded_data)
            except ConnectionResetError:
                print('ConnectionResetError!')
                while self.connect():
                    sleep(1)
                    print("Try to reset connection...")
            except pickle.UnpicklingError:
                print('Pickle error')
                print(data)
            finally:
                del data

    def handle_output(self, writable):
        if self.output_queue:
            for sock in writable:
                for p in self.output_queue:
                    data = pickle.dumps(p)
                    try:
                        sock.send(data)
                        self.output_queue.remove(p)
                    except ConnectionResetError:
                        while self.connect():
                            sleep(1)
                    except ValueError:
                        print('ValueError *** Queue: {}'.format(self.output_queue))

    def send(self, packets):
        try:
            self.lock.acquire()
            self.output_queue += packets
        except LookupError:
            print('Error')
        finally:
            self.lock.release()

    def get_input(self):
        data = copy.copy(self.input_queue)
        self.input_queue.clear()
        return data

    def run(self):
        self.running = True
        clock = pygame.time.Clock()
        while self.running:
            readable, writable, exceptional = select.select([self.socket],
                                                            [self.socket],
                                                            [], 0.0017)
            self.handle_input(readable)
            self.handle_output(writable)
            # clock.tick(60)
import socket
import _pickle
import threading
import select
import pygame

from time import sleep


class TCPClientConnection(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.address = (host, port)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = False
        self.name = -1

        self.output_queue = []
        self.input_queue = []

    def connect(self):
        try:
            self.socket.connect(self.address)
            self.socket.setblocking(False)
            return False
        except OSError:
            return True

    def handle_input(self, sockets):
        for socket in sockets:
            data = None
            try:
                data = socket.recv(1024)
                if data:
                    self.output_queue.append(_pickle.loads(data))
                    print(_pickle.loads(data))
            except ConnectionResetError:
                print('ConnectionResetError!')
                while self.connect():
                    sleep(1)
                    print("Try to reset connection...")
            except _pickle.UnpicklingError:
                pass
            finally:
                del data

    def handle_output(self, sockets):
        if self.output_queue:
            for socket in sockets:
                socket.send(_pickle.dumps(self.output_queue.pop(0)))

    def send(self, packets):
        self.output_queue += packets

    def get_input(self):
        _data = self.output_queue
        self.output_queue.clear()
        return _data

    def run(self):
        self.running = True
        while self.running:
            readable, writable, exceptional = select.select([self.socket],
                                                            [self.socket],
                                                            [], 0)
            self.handle_input(readable)
            self.handle_output(writable)


if __name__ == '__main__':
    client = TCPClientConnection('localhost', 9090)
    client.start()
    while client.connect():
        sleep(1)
        print("Connection failed!")
    while True:
        client.send([1])
        sleep(0.001)

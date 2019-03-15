import socket
import pickle
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

    def handle_input(self, sockets):
        for socket in sockets:
            data = None
            try:
                data = socket.recv(1024)
                if data:
                    self.input_queue.append(pickle.loads(data))
            except ConnectionResetError:
                print('ConnectionResetError!')
                while self.connect():
                    sleep(1)
                    print("Try to reset connection...")
            except pickle.UnpicklingError:
                pass
            finally:
                del data

    def handle_output(self, sockets):
        if self.output_queue:
            for socket in sockets:
                for p in self.output_queue:
                    data = pickle.dumps(p)
                    try:
                        socket.send(data)
                        self.output_queue.remove(p)
                    except ConnectionResetError:
                        while self.connect():
                            sleep(1)

    def send(self, packets):
        try:
            self.lock.acquire()
            self.output_queue += packets
        except LookupError:
            pass
        finally:
            self.lock.release()
        print(self.output_queue)

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
        client.send([['Danya'], ['loh']])
        sleep(0.001)

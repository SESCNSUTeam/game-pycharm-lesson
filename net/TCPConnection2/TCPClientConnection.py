import threading
import socket
import pickle
import select
import time
import copy


class TCPClientConnection(threading.Thread):
    def __init__(self, host, port):
        super().__init__(target=self.run)
        self.running = False
        self.output = []
        self.input = []
        self.lock = threading.Lock()

        self.address = (host, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.socket.connect(self.address)
            self.socket.setblocking(False)
            return False
        except OSError:
            return True

    def send(self, packets):
        try:
            self.lock.acquire()
            self.output += packets
        except LookupError:
            print('LookupError!')
        finally:
            self.lock.release()

    def get_input(self):
        data = copy.copy(self.input)
        self.input.clear()
        return data

    def handle_writable(self, writable):
        if writable:
            if self.output:
                writable[0].sendall(pickle.dumps(self.output))
                self.output.clear()

    def handle_readable(self, readable):
        if readable:
            try:
                data = readable[0].recv(262144)
                if data:
                    self.input.append(pickle.loads(data))
            except ConnectionResetError:
                while self.connect():
                    time.sleep(1)
            except pickle.UnpicklingError:
                print("Unpickling Error!")

    def run(self):
        self.running = True
        while self.running:
            readable, writable, exceptional = select.select([self.socket],
                                                            [self.socket],
                                                            [self.socket], 0)
            self.handle_writable(writable)
            self.handle_readable(readable)


if __name__ == '__main__':
    client = TCPClientConnection()
    client.connect()
    client.start()
    while True:
        if client.input:
            print(client.input)
            client.input.clear()
        client.send([[1, 1, 1, "hello from client"]])
        time.sleep(1 / 1000)

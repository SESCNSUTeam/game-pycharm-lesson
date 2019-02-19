import asyncore
import threading
import _pickle
import socket


class Client(asyncore.dispatcher, threading.Thread):
    def __init__(self, host, port, name):
        self.address = (host, port)
        asyncore.dispatcher.__init__(self)
        threading.Thread.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = name

        self.input = []
        self.data_to_write = []

    def conn(self):
        self.connect(self.address)

    def get_input(self):
        inp = {self.name: self.input}
        self.input = []
        return inp

    def add_output_data(self, data):
        for obj in data:
            self.data_to_write.append(obj)

    def handle_connect(self):
        print("Successfully connected to {}".format(self.address[0]))

    def handle_error(self):
        print("Client error occurred!")

    def handle_write(self):
        if self.data_to_write:
            self.send(_pickle.dumps(self.data_to_write.pop(0)))

    def handle_read(self):
        data = self.recv(1024)
        if data:
            self.input.append(_pickle.loads(data))

    def run(self):
        asyncore.loop()


if __name__ == '__main__':
    pass

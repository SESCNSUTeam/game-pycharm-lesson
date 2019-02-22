import asyncore
import socket
import threading
from server.ClientHandler import ClientHandler

MAX_CONNECTIONS = 4


class Server(asyncore.dispatcher, threading.Thread):
    def __init__(self, host, port):
        self.address = (host, port)
        asyncore.dispatcher.__init__(self)
        threading.Thread.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(self.address)
        self.listen(MAX_CONNECTIONS)

        self.data_to_write = []
        self.connections = []

    def get_input(self):
        inp = dict()
        for i in range(len(self.connections)):
            inp[i] = self.connections[i].input
            self.connections[i].input = []
        return inp

    def handle_accept(self):
        info = self.accept()
        if info is not None:
            print("New connection form: {}".format(info))
            self.connections.append(ClientHandler(info[0], len(self.connections)))

    def add_output_data(self, data):
        for obj in data:
            for client in self.connections:
                client.data_to_write.append(obj)

    def run(self):
        asyncore.loop()


if __name__ == '__main__':
    s = Server("localhost", 9090)
    s.start()

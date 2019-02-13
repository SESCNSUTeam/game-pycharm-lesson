import socket
import threading
import config as c
from time import sleep

host = 'localhost'
port = 9090
address = (host, port)


class ServerOutput(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = False
        self.tcp_socket = socket.socket()
        self.tcp_socket.bind(address)
        self.clients = {}

    def broadcast(self):
        pass

    def run(self):
        self.running = True
        print("Output thread started at port {}".format(9090))
        while self.running:
            print("running")
            if self.tcp_socket.accept():

            self.broadcast()
            sleep(0.5)


if __name__ == '__main__':
    out = ServerOutput()
    out.run()

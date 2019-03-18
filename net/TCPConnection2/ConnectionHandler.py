import socket
import threading
import pickle
import select
import copy


class ServerConnectionHandler(threading.Thread):
    def __init__(self, conn, id):
        super().__init__()

        self.id = id
        self.conn = conn
        self.input = []
        self.output = []

    def handle_writable(self, writable):
        if writable:
            if self.output:
                print("sending")
                writable[0].sendall(pickle.dumps(self.output))
                self.output.clear()

    def handle_readable(self, readable):
        if readable:
            data = readable[0].recv(262144)
            if data:
                self.input.append(pickle.loads(data))

    def get_input(self):
        data = copy.copy(self.input)
        self.input.clear()
        return [[self.id, dt] for dt in data]

    def run(self):
        while True:
            readable, writable, exceptional = select.select([self.conn],
                                                            [self.conn],
                                                            [self.conn], 0)
            self.handle_readable(readable)
            self.handle_writable(writable)

import asyncore
import _pickle


class ClientHandler(asyncore.dispatcher):
    def __init__(self, connection, name):
        asyncore.dispatcher.__init__(self, connection)
        self.name = name

        self.data_to_write = []
        self.input = []

    def writable(self):
        return self.connected

    def handle_error(self):
        pass

    def handle_read(self):
        data = self.recv(1024)
        if data:
            self.input.append(_pickle.loads(data))

    def handle_write(self):
        if bool(self.data_to_write):
            data = _pickle.dumps(self.data_to_write.pop(0))
            self.send(data)

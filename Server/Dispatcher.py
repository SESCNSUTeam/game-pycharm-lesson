import asyncore, socket
import _pickle


class ClientHandler(asyncore.dispatcher):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, 9090))

    def handle_connect(self):
        print('Connected to', self.host)

    def handle_close(self):
        self.close()

    def handle_write(self):
        self.send('')

    def handle_read(self):
        print(' ', self.recv(1024))


class ServerHandler(asyncore.dispatcher):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, 9090))

    def handle_accept(self):
        print(self.accept())

    def handle_close(self):
        self.close()

    def handle_write(self):
        self.send(bytes('hfbvlav', encoding="UTF-8"))

    def handle_read(self):
        print(' ', self.recv(1024))
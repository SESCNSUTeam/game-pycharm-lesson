import socket
import _pickle


class TCPClient:
    def __init__(self, connection, id):
        self.connection = connection
        self.id = id
        self.output_queue = []

    @property
    def socket(self):
        return self.connection

    @property
    def id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id


if __name__ == '__main__':
    pass

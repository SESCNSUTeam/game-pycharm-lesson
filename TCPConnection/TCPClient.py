import socket
import _pickle


class TCPClient:
    def __init__(self, connection):
        self.connection = connection

    @property
    def socket(self):
        return self.connection

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, value):
        self._id = value


if __name__ == '__main__':
    pass

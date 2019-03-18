import socket
import threading
import select
import time

from net.TCPConnection2.ConnectionHandler import ServerConnectionHandler

MAX_CONNECTIONS = 4


class TCPServerConnection(threading.Thread):
    def __init__(self, host, port, max_connections, interface):
        super().__init__()

        self.address = (host, port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(self.address)
        self.server_socket.listen(max_connections)
        self.server_socket.setblocking(False)

        self.connections = []
        self.running = False

        self.interface = interface

    def push_data(self, packet):
        for client in self.connections:
            client.output.append(packet)

    def push_data_by_number(self, packet, conn_number):
        for conn in self.connections:
            if conn.id == conn_number:
                conn.output.append(packet)

    def get_input(self):
        data = []
        for conn in self.connections:
            data += conn.get_input()
        return data

    def on_connection(self, conn):
        new_connection = ServerConnectionHandler(conn, len(self.connections))
        new_connection.start()
        self.connections.append(new_connection)
        self.interface.on_connection(len(self.connections) - 1)

    def clean_input(self):
        """Очистка принятых данных, сделано тольско для тестов, вызывать НЕ надо"""
        for conn in self.connections:
            conn.input.clear()

    def stop(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            readable, writable, exceptional = select.select([self.server_socket],
                                                            [self.server_socket],
                                                            [self.server_socket], 0)
            if self.server_socket in readable:
                conn, addr = self.server_socket.accept()
                self.on_connection(conn)


if __name__ == '__main__':
    server = TCPServerConnection()
    server.start()
    while True:
        server.push_data([[1, 1, 1, 'Hello from server!']])
        if server.connections:
            print(server.connections[0].input)
            server.connections[0].input.clear()
        time.sleep(1 / 1000)

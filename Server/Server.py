import threading
import select
import socket
import _pickle
from Server.Dispatcher import ClientHandler
import asyncore


class Server(threading.Thread):
    def __init__(self, addr, port, max_connections):
        super(Server, self).__init__()
        self.ADDERS = (addr, port)
        self.INPUTS = []
        self.OUTPUTS = []
        self.MAX_CONNECTIONS = max_connections

        self.output_queue = []
        self.input_queue = []
        self.pre_output_data = []
        self.running = False
        self.lock = threading.Lock()

        self.server_socket = self.get_non_blocking_server_socket()

    def get_non_blocking_server_socket(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setblocking(0)

        server.bind(self.ADDERS)

        server.listen(self.MAX_CONNECTIONS)

        return server

    def clear_resource(self, resource):
        """
        Метод очистки ресурсов использования сокета
        """
        if resource in self.OUTPUTS:
            self.OUTPUTS.remove(resource)
        if resource in self.INPUTS:
            self.INPUTS.remove(resource)
        resource.close()

        print('closing connection ' + str(resource))

    def handle_readables(self, readables, server):
        """
        Обработка появления событий на входах
        """
        for resource in readables:

            # Если событие исходит от серверного сокета, то мы получаем новое подключение
            if resource is server:
                connection, client_address = resource.accept()
                connection.setblocking(0)
                self.INPUTS.append(connection)
                print("new connection from {address}".format(address=client_address))

            # Если событие исходит не от серверного сокета, но сработало прерывание на наполнение входного буффера
            else:
                data = ""
                try:
                    data = resource.recv(1024)
                # Если сокет был закрыт на другой стороне
                except ConnectionResetError:
                    self.clear_resource(resource)

                if data:
                    # Вывод полученных данных на консоль
                    print("getting data: {data}".format(data=str(_pickle.loads(data))))

                # Если данных нет, но событие сработало, то ОС нам отправляет флаг о полном
                # прочтении ресурса и его закрытии
                else:
                    # Очищаем данные о ресурсе и закрываем дескриптор
                    self.clear_resource(resource)

    def handle_writables(self, writables):
        if self.output_queue:
            for resource in writables:
                try:
                    resource.send(_pickle.dumps(['name1', 'name2'], 2))
                except OSError:
                    self.clear_resource(resource)

    def get_output_queue(self):
        return self.output_queue

    def add_output_data(self, data):
        self.pre_output_data.append(data)

    def run(self):
        print("Server running on {}, via {}".format(self.ADDERS[0], self.ADDERS[1]))
        self.running = True
        self.INPUTS.append(self.server_socket)
        while self.running:
            readables, writables, exceptional = select.select(self.INPUTS, self.OUTPUTS, self.INPUTS)
            self.handle_readables(readables, self.server_socket)
            self.handle_writables(writables)


class Server2(threading.Thread):
    def __init__(self, host, port):
        super(Server2, self).__init__()
        self.host = host
        self.port = port
        self.handler = ClientHandler(host, port)

    def run(self):
        asyncore.loop()


if __name__ == '__main__':
    server = Server('localhost', 9090, 5)
    server.start()

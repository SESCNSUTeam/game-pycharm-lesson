import socket
import select
import time
import threading
import _pickle
from Server.Dispatcher import ServerHandler
import asyncore
MAX_CONNECTIONS = 4
address_to_server = ('localhost', 9090)


class Client(threading.Thread):
    def __init__(self, addr, port, name):
        super(Client, self).__init__()
        self.name = name
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.INPUTS = [self.socket]
        self.ADDRESS = (addr, port)
        self.input_queue = []
        self.output_queue = []
        self.data = None
        self.lock = threading.Lock()

        self.main_loop = False

        self.running = False

    def stop(self):
        self.running = False

    def connect(self):
        self.socket.connect(self.ADDRESS)
        self.socket.setblocking(0)

    def get_input_data(self):
        _return = self.output_queue
        self.output_queue = []
        return _return

    def add_output_data(self, obj):
        with self.lock:
            self.output_queue.append(obj)

    def clear_resource(self, resource):
        """
        Метод очистки ресурсов использования сокета
        """
        if resource in self.INPUTS:
            self.INPUTS.remove(resource)
        resource.close()

    def handle_readables(self, readables, socket):
        for resource in readables:
            try:
                self.data = resource.recv(1024)
            except ConnectionResetError:
                self.clear_resource(resource)

            if self.data:
                print("getting data: {data}".format(data=str(self.data)))

            # Если данных нет, но событие сработало, то ОС нам отправляет флаг о полном
            # прочтении ресурса и его закрытии
            else:
                # Очищаем данные о ресурсе и закрываем дескриптор
                self.clear_resource(resource)

    def send_data(self):
        with self.lock:
            _data = self.output_queue[0]
            self.output_queue.pop(0)
        self.socket.send(_pickle.dumps(['obj1', 'obj2'], 2))

    def run(self):
        self.running = True
        while self.running:
            if self.output_queue:
                print(self.output_queue)
                self.send_data()


class Client2(threading.Thread):
    def __init__(self, host, port):
        super(Client2, self).__init__()
        self.host = host
        self.port = port
        self.handler = ServerHandler(host, port)

    def run(self):
        asyncore.loop()


if __name__ == '__main__':
    client = Client('localhost', 9090, 1)
    print(type(client.INPUT))
    client.start()
    client.send_data()

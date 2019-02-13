import socket
import time
import threading

MAX_CONNECTIONS = 4
address_to_server = ('localhost', 8686)
'''''
clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(MAX_CONNECTIONS)]
for client in clients:
    client.connect(address_to_server)
i = 0
'''''


class Client(threading.Thread):
    def __init__(self, addr, port):
        super(Client, self).__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (addr, port)
        try:
            self.connect(self.address)
        except:
            print("Exception occurred")
            exit()

    def connect(self, addr):
        self.socket.connect(addr)

    def send_data(self):
        self.socket.send(bytes("Hello from client!"))

    def run(self):
        pass


'''''
while True:
    for i in range(MAX_CONNECTIONS):
        clients[i].send(bytes("hello from client number " + str(i), encoding='UTF-8'))
        time.sleep(0.00000001)
        print(clients[i].recv(1024))
'''''

if __name__ == '__main__':
    pass

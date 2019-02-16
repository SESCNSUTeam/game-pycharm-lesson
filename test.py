from Server.Client import Client, Client2
from Server.Server import Server, Server2
from random import randint, choice
from time import sleep
MAX_CONNECTIONS = 4
address_to_server = ('localhost', 9090)

server = Server2(address_to_server[0], address_to_server[1])
clients = [Client2('localhost', 9090) for i in range(MAX_CONNECTIONS)]

server.start()
for i in clients:
    i.start()

from net.TCPConnection2.TCPServerConnection import TCPServerConnection
from net.TCPConnection2.TCPClientConnection import TCPClientConnection


server = TCPServerConnection()
client = TCPClientConnection()

client.connect()

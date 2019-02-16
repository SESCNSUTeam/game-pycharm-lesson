import pickle
import socket
import threading


def server():
    BUFFER_SIZE = 4096
    sock = socket.socket()
    sock.bind(('', 5050))
    sock.listen(1)

    print('Server: Sock name: {}'.format(sock.getsockname()))
    conn, addr = sock.accept()
    print('Server: Connected:', addr)

    while True:

        all_data = bytearray()

        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            elif data == b';':
                break
            # print('Server: Recv: {}: {}'.format(len(data), data))
            all_data += data
        obj = pickle.loads(all_data)
        print('Server: Obj:', obj)

    print('Server: Close')
    conn.close()


def client():
    import socket
    sock = socket.socket()
    sock.connect(('127.0.0.1', 5050))

    obj = {
        'a': 1,
        'b': [2, 3],
        'c': {
            'c1': 'abc',
        }
    }

    print('Client: Send:', obj)

    import pickle
    data = pickle.dumps(obj)
    while True:
        sock.sendall(data)
        sock.send(b';')

    print('Client: Close')
    sock.close()


thread = threading.Thread(target=server)
thread.start()
thread2 = threading.Thread(target=client)
thread2.start()

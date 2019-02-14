import threading
import select
import socket
import asyncio


class Server(threading.Thread):
    def __init__(self, addr, port):
        super(Server, self).__init__()
        self.address = (addr, port)
        self.output_queue = []
        self.input_queue = []
        self.running = False
        self.lock = threading.Lock()

    async def post_data(self):
        print("post data")
    
    async def read_data(self):
        print('reading data')

    def stop_server(self):
        self.running = False

    def get_input(self):
        return 
    
    def get_output_queue(self):
        return self.output_queue

    def add_output_data(self, data):
        print('add_output_data')
        try:
            self.lock.acquire(True)
            self.output_queue.append(data)
        finally:
            self.lock.release()

    def run(self):
        self.running = True
        main_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(main_loop)
        main_loop = asyncio.get_event_loop()
        tasks = [
            main_loop.create_task(self.post_data()),
            main_loop.create_task(self.read_data())
        ]
        while self.running:
            main_loop.run_until_complete(asyncio.tasks)


if __name__ == '__main__':
    server = Server('localhost', 9090)
    server.start()
    server.add_output_data(1)
    print(server.output_queue)

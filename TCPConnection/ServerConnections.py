class ServerConnections:
    def __init__(self):
        self.connections = []

    def new_connection(self, socket):
        if socket not in self.connections:
            self.connections.append({})

    def set_id(self):
        pass

    def get_connections(self):
        return self.connections

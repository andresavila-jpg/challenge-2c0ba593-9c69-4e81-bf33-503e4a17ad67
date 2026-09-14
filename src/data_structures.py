class Client:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city
        self.purchases: list = []
        self.transactions: list = []

class ClientArray:
    def __init__(self):
        self.clients = []

    def add_client(self, client: Client):
        self.clients.append(client)

    def find_client_by_name(self, name: str) -> Client:
        for client in self.clients:
            if client.name == name:
                return client
        raise ValueError('Client not found')

class ClientList:
    def __init__(self):
        self.clients = []

    def add_client(self, client: Client):
        self.clients.append(client)

    def find_client_by_name(self, name: str) -> Client:
        for client in self.clients:
            if client.name == name:
                return client
        raise ValueError('Client not found')
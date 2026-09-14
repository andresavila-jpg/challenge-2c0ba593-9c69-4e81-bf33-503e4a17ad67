from src.data_structures import Client


class ClientDict:
    def __init__(self):
        self.clients = {}

    def add_client(self, client: Client):
        self.clients[client.name] = client

    def find_client_by_name(self, name: str) -> Client:
        if name in self.clients:
            return self.clients[name]
        raise ValueError('Client not found')

    def add_purchase(self, name: str, purchase: int):
        if name in self.clients:
            self.clients[name].purchases.append(purchase)
        else:
            raise ValueError('Client not found')

    def get_total_purchases(self, name: str) -> int:
        if name in self.clients:
            return sum(self.clients[name].purchases)
        raise ValueError('Client not found')

class ClientMatrix:
    def __init__(self):
        self.clients = {}

    def add_client(self, client: Client):
        self.clients[client.name] = client

    def find_client_by_name(self, name: str) -> Client:
        if name in self.clients:
            return self.clients[name]
        raise ValueError('Client not found')

    def add_transaction(self, name: str, transaction: int):
        if name in self.clients:
            self.clients[name].transactions.append(transaction)
        else:
            raise ValueError('Client not found')

    def get_total_transactions(self, name: str) -> int:
        if name in self.clients:
            return sum(self.clients[name].transactions)
        raise ValueError('Client not found')
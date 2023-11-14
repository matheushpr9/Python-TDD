from Client import Client
class System:

    def __init__(self) -> None:
        self.registered_clients = []

    def client_registration(self, client: Client):
        self.registered_clients.append(client)
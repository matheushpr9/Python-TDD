from classes.Client import Client
from classes.System import System

def test_client_successfully_registered():
    client = Client("Thales", 28, "th@gmail.com")
    system = System()
    response = system.client_registration(client)
    assert "Client successfully registered!" == response
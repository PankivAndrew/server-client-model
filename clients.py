from constants import HOST, PORT, NUM_CLIENTS
from utils import create_clients
import time

clients = create_clients(NUM_CLIENTS, HOST, PORT)

for _ in range(10):
    for index, client in enumerate(clients):
        client.send()
    time.sleep(1)

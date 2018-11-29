from models import Client


def create_clients(num_objects, host, port):
    return [Client(host, port, i + 1) for i in range(num_objects)]

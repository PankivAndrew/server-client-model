import socket
import threading
import time
import json


class Server(object):
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen()
        self.threads = []

    def start(self, num_workers):
        for _ in range(num_workers):
            thread = threading.Thread(target=self.worker)
            thread.start()
            self.threads.append(thread)
        self.join()

    def join(self):
        for thread in self.threads:
            thread.join()

    def worker(self):
        conn, addr = self.socket.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                data = json.loads(data.decode())
                print("Receive: {}".format(data))
                data['timestamp'] = int(time.time() * 1000)
                conn.sendall(json.dumps(data).encode())
                print()


class Client(object):
    def __init__(self, host, port, id):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.data = {'id': id}

    def send(self):
        self.data['timestamp'] = int(time.time() * 1000)
        self.socket.sendall(json.dumps(self.data).encode())
        print('Receive form server: {}'.format(self.socket.recv(1024).decode()))
        print()


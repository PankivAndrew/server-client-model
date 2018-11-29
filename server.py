from models import Server
from constants import HOST, PORT, NUM_CLIENTS


server = Server(HOST, PORT)
server.start(NUM_CLIENTS)

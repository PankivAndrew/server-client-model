from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
NUM_CLIENTS = int(os.getenv('NUM_CLIENTS'))

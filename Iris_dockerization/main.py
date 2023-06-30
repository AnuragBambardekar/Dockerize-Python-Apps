import time
import socket
from sklearn.datasets import load_iris

data = load_iris()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))

server.listen()

while True:
    client, addr = server.accept()
    print("Connection from: ", addr)
    client.send("You are connected!\n".encode())
    client.send(f"{data['data'][:, 0]}\n".encode())

    time.sleep(2)
    client.send("You are being disconnected!\n".encode())
    client.close()

# Using telnet
# Go to Windows features and enable telnet client
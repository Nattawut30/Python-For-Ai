# use this file with sockets_network.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080)) # Change it to connect
message = s.recv(1024) # Specify how many bytes to read!
s.close()

print(message.decode())

# result:
# client.py = You are connected!
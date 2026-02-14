# Sockets and Network Programming
# use this file with client.py

# how to send a data over the networks
# how to exchange data
# how to build connections between clients and servers

# socket = the end point of a communication channel.
# so when you have a communication in a network you always have a 2 end points.
# these end points are called socket. just 2 socket that try to exchange something
# The end points of communication channels

# Deal with socket is dealing with the lower levels of connectivity
# The connection oriented protocol TCP, and the connection oriented connectionless protocol
# pick a port that not commonly used

# socket.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8080)) # local host IP address & Port
s.listen() # server, puts our socket into listening mode to possible connection

while True:
    client, address = s.accept() # use when client tries to connect to the server
    print("Connected to ()".format(address))
    client.send("You are connected!".encode())
    client.close() # just closing it so that we don't have unlimited amount of clients

# result:
# socket.py = Connected to ('127.0.0.1', 51390)
# sometimes port is not the same. does not matter. it's the IP address!
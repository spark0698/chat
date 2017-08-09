#!/usr/local/bin/python

import socket
import sys

class BasicServer(object):

    def __init__(self, port):
        self.port = int(port)
        self.socket = socket.socket()

    def setup(self):
        self.socket.bind(("localhost",self.port))
        self.socket.listen(5)

    def recv(self):
        (new_sock, client_addr) = self.socket.accept()
        return new_sock.recv(1024)

args = sys.argv
if len(args) != 2:
    print "Please supply a port number."
    sys.exit()

server = BasicServer(args[1])
server.setup()

while True:
    Data = server.recv()
    if Data == "":
        pass
    else:
        print Data

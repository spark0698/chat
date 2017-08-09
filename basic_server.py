#!/usr/local/bin/python

import socket
import sys

class BasicServer(object):

    def __init__(self, port):
        self.port = int(port)
        self.socket = socket.socket()

    def recv(self):
        self.socket.bind(("127.0.0.1",self.port))
        self.socket.listen(5)
        (new_sock, client_addr) = self.socket.accept()
        return new_sock.recv(1024)

args = sys.argv
if len(args) != 2:
    print "Please supply a port number."
    sys.exit()

server = BasicServer(args[1])

Data = server.recv()
print Data

#!/usr/bin/python3
import sys
import socket as sock

client_socket = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)

# my_req = "google.com"
client_socket.sendto(bytes(sys.argv[1], 'utf-8'), ("127.0.0.1", 1053))

data, ipaddress = client_socket.recvfrom(1000)
client_socket.close()
print(data.decode())

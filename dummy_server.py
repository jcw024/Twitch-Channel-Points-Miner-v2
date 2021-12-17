import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 7777
BUFFER_SIZE = 1024

print("starting server...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen()
conn, addr = s.accept()
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    else:
        print("received data: ", data)

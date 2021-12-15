
import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 7777
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
i = 0
print("starting to send dummy messages... CTRL+C to quit")
while 1:
    print(f"sending message {i}")
    s.send(bytes(f"sending message #{i}",'utf-8'))
    time.sleep(1)
    i += 1
data = s.recv(BUFFER_SIZE)
s.close()


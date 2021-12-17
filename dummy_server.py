import socket
from threading import Thread
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 7777
BUFFER_SIZE = 1024

def on_new_client(conn, addr):
    while True:
        data = conn.recv(BUFFER_SIZE)
        print(data, flush=True)
        if not data: break
        conn.sendall(data)
    print(addr, " closed", flush=True)
    conn.close()

print("starting server...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((TCP_IP, TCP_PORT))
    s.listen()
    while 1:
        conn, addr = s.accept()
        print(addr, " connected")
        t = Thread(target=on_new_client, args=(conn,addr))
        t.start()

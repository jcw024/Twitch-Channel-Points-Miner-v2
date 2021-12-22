import socket
import time
import json
from dummy_data import *
from threading import Thread

TCP_IP = '127.0.0.1'
TCP_PORT = 7778
BUFFER_SIZE = 2048

def on_new_client(conn, addr, SPARK_SOCKET):
    while True:
        data = conn.recv(BUFFER_SIZE)
        print(data, flush=True)
        if not data: break
        SPARK_SOCKET.send(data+b'\n')
    print(addr, " closed", flush=True)
    conn.close()

print("starting server... (startup spark first)")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((TCP_IP, TCP_PORT))
    s.listen()
    SPARK_SOCKET, addr = s.accept()
    #while 1:
    #    #SPARK_SOCKET.send(b'test data\n')
    #    SPARK_SOCKET.send(json.dumps(EVENT_CREATED).encode("utf-8")+b'\n')
    #    print("data sent")
    #    time.sleep(3)
    print("spark client connected...")
    while 1:
        clientsocket, addr = s.accept()
        print(addr, " connected")
        t = Thread(target=on_new_client, args=(clientsocket,addr, SPARK_SOCKET))
        t.start()

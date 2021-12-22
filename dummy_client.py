from dummy_data import EVENT_CREATED, POINTS_SPENT, POINTS_EARNED, CLAIM_AVAILABLE, CLAIM_CLAIMED, PREDICTION_RESULT
import socket
import time
import json

TCP_IP = '127.0.0.1'
TCP_PORT = 7778
BUFFER_SIZE = 2048

dummy_data_list = [EVENT_CREATED, POINTS_SPENT, POINTS_EARNED, CLAIM_AVAILABLE, CLAIM_CLAIMED, PREDICTION_RESULT]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
i = 0
print("starting to send dummy messages... CTRL+C to quit")
while 1:
    for data in dummy_data_list:
        print(f"sending message type: {data['type']}")
        #s.send(bytes(f"sending message #{i}",'utf-8'))
        i += 1
        s.send(json.dumps(data).encode("utf-8"))
        #data_recv = s.recv(BUFFER_SIZE)
        #print(f"received data: {data_recv}")
        time.sleep(3)
        s.close()
        print("socket closed")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))


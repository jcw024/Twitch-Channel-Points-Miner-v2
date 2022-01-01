from dummy_data import EVENT_CREATED, POINTS_SPENT, POINTS_EARNED, CLAIM_AVAILABLE, CLAIM_CLAIMED, PREDICTION_RESULT
import time
import json
from kafka import KafkaProducer

#dummy_data_list = [EVENT_CREATED, POINTS_SPENT, POINTS_EARNED, CLAIM_AVAILABLE, CLAIM_CLAIMED, PREDICTION_RESULT]
dummy_data_list = [PREDICTION_RESULT]
#bootstrap_broker_string = "b-3.twitchminer.cjp8yc.c11.kafka.us-west-2.amazonaws.com:9094,b-2.twitchminer.cjp8yc.c11.kafka.us-west-2.amazonaws.com:9094,b-1.twitchminer.cjp8yc.c11.kafka.us-west-2.amazonaws.com:9094"
bootstrap_broker_string = "localhost:9092"
BUFFER_SIZE = 16384 

if __name__ == "__main__":
    #execute producer.py to test on small dataset
    producer = KafkaProducer(bootstrap_servers=bootstrap_broker_string, linger_ms=1000, batch_size=BUFFER_SIZE)
    while 1:
        for data in dummy_data_list:
            if len(data) <= 1: continue
            data = json.dumps(data).encode("utf-8")
            producer.send('test', data)
            print(f"send data: {data}")
            time.sleep(3)

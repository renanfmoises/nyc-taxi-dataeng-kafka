from multiprocessing.sharedctypes import Value
from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], # Kafka local dockerized server
                         value_serializer=lambda x:
                            dumps(x).encode('utf-8'))

for i in range(1000):
    data = {'number' : i}
    producer.send('demo_topic', value=data)
    print('produced:', data)
    sleep(1)

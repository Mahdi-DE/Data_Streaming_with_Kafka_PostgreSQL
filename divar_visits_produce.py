from kafka import KafkaProducer
import json
import string
import random
import time


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8'))


for j in range(1000):

    time.sleep(20)

    address = str()
    N = 7
    for i in range(4):
        x = ''.join(random.choices(string.ascii_uppercase +
                                    string.digits, k=N))+"-"
        address += x
        
    address = address[:-1]   
    
    age = random.randint(18, 110)

    phone_number = ''.join(random.choices(string.digits, k=11))
    
    data = {'address': address,'age':age,'phone_number':phone_number}

    producer.send('test', value=data)

    print(data)

    
producer.flush()


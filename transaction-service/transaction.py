import json
import time
import uuid
import logging
import faker
import random
from datetime import datetime
from kafka import KafkaProducer, KafkaConsumer

logging.basicConfig(level=logging.INFO)

# create kafka topic

ORDER_KAFKA_TOPIC = "order-details"
ORDER_PROCESSED_KAFKA_TOPIC = "order-processed"
# BOOT_STRAP_SERVERS = 'kafka-local.orders-microservice.svc.cluster.local:9092'
BOOT_STRAP_SERVERS = 'localhost:9092'
ORDER_LIMIT = 10

# consumer
consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC,
    bootstrap_servers=BOOT_STRAP_SERVERS
)

producer = KafkaProducer(bootstrap_servers=BOOT_STRAP_SERVERS)

if __name__ == '__main__':
    # print(create_orders())
    logging.info('Started processing transactions...')

    while True:
        for message in consumer:
            consumed_msg = json.loads(message.value.decode('utf-8'))

            # process transaction

            username = consumed_msg['username']
            quantity = consumed_msg['quantity']
            price = consumed_msg['price']
            total_cost = round(float(quantity * price), 2)

            data = {
                'order_id': consumed_msg['order_id'],
                'username': username,
                'email': consumed_msg['email'],
                'total_cost': total_cost
            }

            logging.info(f"Order {data['order_id']} processed")

            # send processed order to kafka
            producer.send(ORDER_PROCESSED_KAFKA_TOPIC, json.dumps(data).encode('utf-8'))
            time.sleep(3)


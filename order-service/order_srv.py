import json
import time
import uuid
import logging
import faker
import random
from datetime import datetime
from kafka import KafkaProducer

logging.basicConfig(level=logging.INFO)

# create kafka topic

ORDER_KAFKA_TOPIC = "order-details"
ORDER_LIMIT = 15

producer = KafkaProducer(bootstrap_servers='kafka-local.orders-microservice.svc.cluster.local:9092')

def create_orders():
    f = faker.Faker()
    orders = dict(
        order_id=str(uuid.uuid4()),
        username=f.user_name(),
        first_name=f.first_name(),
        last_name=f.last_name(),
        email=f.email(),
        queantity=int(random.randint(1, 999)),
        price=round(float(random.uniform(10.5, 100.99)), 2),
        date_created=str(datetime.now())
    )

    return orders


if __name__ == '__main__':
    # print(create_orders())
    logging.info('Generating orders...')

    for order in range(ORDER_LIMIT):
        data = create_orders()

        #send orders to kafka topic
        producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode('utf-8'))
        logging.info(f"Order {data['order_id']} sent to kafka topic")
        time.sleep(1)

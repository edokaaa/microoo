import json
import logging
from kafka import KafkaConsumer

logging.basicConfig(level=logging.INFO)

ORDER_PROCESSED_KAFKA_TOPIC = "order-processed"
BOOT_STRAP_SERVERS = 'kafka-local.orders-microservice.svc.cluster.local:9092'
# BOOT_STRAP_SERVERS = 'localhost:9092'

# consumer
consumer = KafkaConsumer(
    ORDER_PROCESSED_KAFKA_TOPIC,
    bootstrap_servers=BOOT_STRAP_SERVERS
)

if __name__ == '__main__':
    total_order_count = 0
    total_revenue = 0.0

    logging.info('Started order analytics...')

    while True:
        for message in consumer:
            logging.info("Updating analytics service...")
            consumed_msg = json.loads(message.value.decode('utf-8'))
            total_cost = float(consumed_msg['total_cost'])
            total_order_count += 1
            total_revenue += total_cost

            logging.info(f"Total order count: {total_order_count}")
            logging.info(f"Total revenue: {round(total_revenue, 2)}")

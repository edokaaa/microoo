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
    emails_sent = set()


    logging.info('Started sending out emails...')

    while True:
        for message in consumer:
            consumed_msg = json.loads(message.value.decode('utf-8'))
            customer_email = consumed_msg['email']
            logging.info(f"Sending email to {customer_email}")
            emails_sent.add(customer_email)
            # send email
            logging.info(f"Emails sent: {len(emails_sent)}")

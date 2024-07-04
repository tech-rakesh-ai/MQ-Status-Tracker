import pika
import json
from datetime import datetime
from apps.db_conn import init_mongo_db

from apps import settings

DB_NAME = settings.MONGO_DB
COLLECTION_NAME = settings.MONGO_COLLECTION


def process_message(ch, method, properties, body):
    message = json.loads(body)
    message['timestamp'] = datetime.utcnow()
    client = init_mongo_db()
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    collection.insert_one(message)
    print(f"Received: {message}")


def start_mqtt_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=settings.RABBITMQ_QUEUE_NAME)
    channel.basic_consume(queue=settings.RABBITMQ_QUEUE_NAME, on_message_callback=process_message, auto_ack=True)
    print('----------My Mqtt Consumer is waiting for messages. To exit press CTRL+C ------------------')
    print("connection----------------", connection)
    print("channel-------------------", channel)
    channel.start_consuming()

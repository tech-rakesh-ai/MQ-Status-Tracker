import pika
import json
import time
import random

from apps import settings


# MQTT message generation
def generate_mqtt_message():
    return json.dumps({"status": random.randint(0, 6)})


def main():
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.RABBITMQ_HOST))
    channel = connection.channel()
    print("connection---------------->", connection)
    print("channel------------------->", channel)

    # Declare a queue
    channel.queue_declare(queue=settings.RABBITMQ_QUEUE_NAME)

    try:
        while True:
            message = generate_mqtt_message()
            channel.basic_publish(exchange='', routing_key=settings.RABBITMQ_QUEUE_NAME, body=message)
            print(f"Msg Sent: {message}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Client stopped.")
    finally:
        connection.close()


if __name__ == '__main__':
    main()

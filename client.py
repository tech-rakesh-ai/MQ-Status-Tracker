import pika
import json
import time
import random

# RabbitMQ configuration
rabbitmq_host = 'localhost'
rabbitmq_queue = 'mqtt_queue'


# MQTT message generation
def generate_mqtt_message():
    return json.dumps({"status": random.randint(0, 6)})


def main():
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue=rabbitmq_queue)

    try:
        while True:
            message = generate_mqtt_message()
            channel.basic_publish(exchange='',
                                  routing_key=rabbitmq_queue,
                                  body=message)
            print(f"Sent: {message}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Client stopped.")
    finally:
        connection.close()


if __name__ == '__main__':
    main()

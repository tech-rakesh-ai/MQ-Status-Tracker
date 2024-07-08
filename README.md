# MQ Status Tracker

## Project Description

This project implements a client-server architecture that handles MQTT messages via RabbitMQ. The client script emits
MQTT messages every second containing a field "status" with a random value in the range of 0-6. The server processes
these messages and stores them in MongoDB. Additionally, the server provides an endpoint to accept start and end times
and return the count of each status during the specified time range.

## Basic Flow of MQTT using `pika` Library

1. **Client Script**:
    - Connects to RabbitMQ.
    - Emits MQTT messages every second with a "status" field containing a random value between 0 and 6.

2. **Server Script**:
    - Connects to RabbitMQ to receive MQTT messages.
    - Processes and stores the messages in MongoDB.
    - Provides an endpoint to retrieve the count of each status within a specified time range using FastAPI.

## Getting Started

### Prerequisites

- Install Python (version 3.8 or higher).
- Install MongoDB.
- Install RabbitMq.

### Clone the Repository

1. Clone:

   ```shell
   git clone https://github.com/tech-rakesh-kr/MQ-Status-Tracker.git
   cd MQ-Status-Tracker
   ```

2. Create a virtual environment:

   ```shell
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Run the Backend
    ```shell
   python main.py
   ```
5. Run the Frontend(client)

   ```shell
   python client.py
   ```
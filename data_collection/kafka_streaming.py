from kafka import KafkaConsumer
import logging
from flask_socketio import SocketIO, emit

socketio = SocketIO(message_queue='redis://')  # Assuming Redis is used as the message queue

def stream_data_from_kafka(topic):
    """Streams data from a Kafka topic and processes each message.

    Args:
        topic (str): The name of the Kafka topic to consume.
    """

    logging.basicConfig(level=logging.DEBUG)  

    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092')
    for message in consumer:
        logging.debug(f"Received message: {message.value}")
        process_message(message.value)

def process_message(message):
    """Processes a received message.

    Args:
        message (bytes): The message content.
    """

    logging.debug(f"Processing message: {message}")
    socketio.emit('update', {'text': message.decode('utf-8')})

if __name__ == "__main__":
    topic = "realtime"
    stream_data_from_kafka(topic)
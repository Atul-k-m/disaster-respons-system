from kafka import KafkaConsumer
import logging

def stream_data_from_kafka(topic):
    """Streams data from a Kafka topic and processes each message.

    Args:
        topic (str): The name of the Kafka topic to consume.
    """

    logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG

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

if __name__ == "__main__":
    topic = "realtime"
    stream_data_from_kafka(topic)
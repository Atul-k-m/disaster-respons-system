from flask import Flask, jsonify
from app.routes import app  # Import the entire app instance
from flask_cors import CORS
from flask_socketio import SocketIO
from data_collection.kafka_streaming import stream_data_from_kafka

CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return 'Socket.IO server running'

if __name__ == '__main__':
    # Start Kafka streaming in a separate thread
    import threading
    kafka_thread = threading.Thread(target=stream_data_from_kafka, args=('disaster_topic',))
    kafka_thread.start()
    
    socketio.run(app, debug=True)
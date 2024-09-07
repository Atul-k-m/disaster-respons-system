from bson import ObjectId
from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
import threading
from data_collection.kafka_streaming import stream_data_from_kafka
from data_collection.api_fetcher import fetch_news_data
from nlp_processing.text_analysis import sentiment_analysis
from app.models import store_data
from app.utils import setup_logging, log_message
import socketio

def create_app():
    app = Flask(__name__)
    CORS(app)
    socketio = SocketIO(app, cors_allowed_origins="*")
    setup_logging()

    @app.route('/fetch-data', methods=['GET'])
    def fetch_data():
        query = "earthquake OR flood OR wildfire"
        try:
            log_message('Fetching data from APIs...')
            news_data = fetch_news_data(query)
            log_message(f'Fetched raw data: {news_data}')  # raw data
        except Exception as e:
            return jsonify({"error": f"Error fetching data: {str(e)}"}), 500

        processed_data = []
        for item in news_data.get('articles', []):
            if 'title' in item and item['title']:
                sentiment = sentiment_analysis(item['title'])
                #collection
                processed_data.append({
                    'title': item['title'],
                    'sentiment': sentiment
                })
            else:
                log_message(f"Skipping item with no text: {item}")  

        if not processed_data:
            log_message("No processed data to store.")
            return jsonify({"error": "No data to store"}), 400

        try:
            store_data('disaster_data', processed_data)
            log_message(f'Stored data: {processed_data}')
        except Exception as e:
            return jsonify({"error": f"Error storing data: {str(e)}"}), 500

        for item in processed_data:
            if "_id" in item and isinstance(item["_id"], ObjectId):
                item["_id"] = str(item["_id"])

        return jsonify({"data": processed_data})

    @app.errorhandler(Exception)
    def handle_exception(error):
        return jsonify({"error": str(error)}), 500

    return app

app = create_app()

if __name__ == '__main__':
    kafka_thread = threading.Thread(target=stream_data_from_kafka, args=("realtime",))
    kafka_thread.start()
    socketio.run(app, debug=True)
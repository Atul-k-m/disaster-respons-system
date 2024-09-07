from pymongo import MongoClient
from flask import Flask, jsonify
from flask import jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
import socketio
from data_collection.api_fetcher import fetch_news_data
from nlp_processing.text_analysis import sentiment_analysis
from app.models import store_data
from app.utils import setup_logging, log_message

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
            log_message(f'Fetched raw data: {news_data}')  # Log the raw data
        except Exception as e:
            return jsonify({"error": f"Error fetching data: {str(e)}"}), 500

        processed_data = []
        for item in news_data.get('articles', []):
            # Check if 'text' is present in each item
            if 'title' in item and item['title']:
                sentiment = sentiment_analysis(item['title'])
                processed_data.append({
                    'title': item['title'],
                    'sentiment': sentiment
                })
            else:
                log_message(f"Skipping item with no text: {item}")  # Log items that are skipped

        if not processed_data:
            log_message("No processed data to store.")
            return jsonify({"error": "No data to store"}), 400

        try:
            store_data('disaster_data', processed_data)
            log_message(f'Stored data: {processed_data}')
        except pymongo.errors.DuplicateKeyError as e:
             log_message(f"Duplicate key error: {str(e)}")
             return jsonify({"error": "Duplicate key error"}), 400
        except Exception as e:
            return jsonify({"error": f"Error storing data: {str(e)}"}), 500

        return jsonify({"data": processed_data})

    @app.errorhandler(Exception)
    def handle_exception(error):
        return jsonify({"error": str(error)}), 500

    return app

app = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=True)

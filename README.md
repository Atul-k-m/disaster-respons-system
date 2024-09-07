# Disaster-Response-System

A system that collects, processes, and visualizes disaster data in real-time, providing insights and analysis for better decision-making during disaster management efforts.

## Features

- Fetches disaster data from various APIs.
- Processes and stores data in MongoDB.
- Provides real-time updates using Socket.IO.
- Visualizes disaster data using charts.
  
## Project Structure

- **app/**: Contains the Flask backend application code.
- **data_collection/**: Contains scripts for data collection from APIs and Kafka streaming.
- **frontend/**: Contains the React frontend code.
- **nlp_processing/**: Contains scripts for text analysis and classification.
- **models/**: Contains scripts for data storage in MongoDB.
- **utils/**: Contains utility functions for logging and other helper methods.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Node.js
- MongoDB
- Kafka

## Installation

### Backend (Flask)

1. Clone the repository:

   `git clone https://github.com/yourusername/Disaster-Response-System.git`
   `cd Disaster-Response-System`

2. Navigate to the `app/` directory and install dependencies:


   `python3 -m venv venv`
   `source venv/bin/activate   # For Windows: venv\Scripts\activate`
   `pip install -r requirements.txt`

3. Set up environment variables (e.g., API keys, database URIs) in a `.env` file in the `app/` directory.

4. Start the Flask backend:

   `flask run`

   The backend runs at [http://localhost:5000](http://localhost:5000).

### Frontend (React)

1. Navigate to the `frontend/` directory:

   `cd ../frontend`

2. Install dependencies:

   `npm install`

3. Start the React frontend:

   `npm start`

   The frontend runs at [http://localhost:3000](http://localhost:3000).

### Data Collection (Kafka)

1. Make sure Kafka is running locally or in a cloud environment.
2. Run data collection scripts inside the `data_collection/` folder to stream disaster-related data from APIs to your Kafka topics.

### MongoDB Setup

1. Start your local or remote MongoDB instance.
2. Configure your MongoDB URI in the backend `.env` file to connect to the correct database.

## Usage

Access the frontend at [http://localhost:3000](http://localhost:3000).  
The backend runs at [http://localhost:5000](http://localhost:5000).

The system will collect disaster data, process it, and visualize the information in real-time.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure all pull requests follow the project's code style and include tests where appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

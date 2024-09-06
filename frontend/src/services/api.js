// api.js
import axios from 'axios';

export const fetchDisasterData = async () => {
  try {
    const response = await axios.get('http://localhost:5000/fetch-data');
    return response.data;
  } catch (error) {
    console.error('Error fetching disaster data', error);
    throw error;
  }
};

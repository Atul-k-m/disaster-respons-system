import axios from 'axios';

export const fetchDisasterData = async () => {
  try {
    console.log('Fetching disaster data from backend...');
    const response = await axios.get(`http://localhost:5000/fetch-data`);
    console.log('Fetched data:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error fetching disaster data:', error);
    throw error;
  }
};
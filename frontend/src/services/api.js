import axios from 'axios';

export const fetchDisasterData = async () => {
  try {
    console.log('Fetching disaster data from backend...');
    const response = await axios.get(`${process.env.REACT_APP_API_URL}/fetch-data`);
    console.log('Fetched data:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error fetching disaster data:', error);
    throw error;
  }
};
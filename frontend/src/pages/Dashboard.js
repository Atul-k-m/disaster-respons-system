import React, { useEffect, useState } from 'react';
import DisasterChart from '../components/DisasterChart';
import RealTimeUpdates from '../components/RealTimeUpdates';
import { fetchDisasterData } from '../services/api';

const Dashboard = () => {
  const [disasterData, setDisasterData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        console.log('Fetching disaster data...');
        const response = await fetchDisasterData();
        console.log('Data received:', response);
        if (response.data) {
          console.log('Processed data:', response.data);
          setDisasterData(response.data);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Disaster Response Dashboard</h1>
      <DisasterChart disasterData={disasterData} />
      <RealTimeUpdates />
    </div>
  );
};

export default Dashboard;
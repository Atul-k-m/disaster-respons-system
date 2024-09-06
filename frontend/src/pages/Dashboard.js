import React, { useEffect, useState } from 'react';
import DisasterChart from '../components/DisasterChart';
import RealTimeUpdates from '../components/RealTimeUpdates';
import { fetchDisasterData } from '../services/api';

const Dashboard = () => {
  const [disasterData, setDisasterData] = useState([]);

  useEffect(() => {
    const loadData = async () => {
      const data = await fetchDisasterData();
      setDisasterData(data);
    };

    loadData();
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

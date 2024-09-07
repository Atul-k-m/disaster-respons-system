import React, { useEffect, useState } from 'react';
import Card from '../components/Card';
import DisasterChart from '../components/DisasterChart';
import RealTimeUpdates from '../components/RealTimeUpdates';
import { fetchDisasterData } from '../services/api';

const Dashboard = () => {
  const [disasterData, setDisasterData] = useState([]);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetchDisasterData();
        if (response.data) {
          setDisasterData(response.data);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
  
    fetchData();
  
    
    const interval = setInterval(() => {
      fetchData();
    }, 3 * 60 * 1000); // 3 min refresh
  
    return () => clearInterval(interval); 
  }, []);

  return (
    <div className="dashboard">
      <h1>Disaster Response Dashboard</h1>
      <div className="cards">
        {disasterData.map((item, index) => (
          <Card 
            key={index} 
            title={item.title} 
            content={
              item.sentiment.map((sent, i) => (
                <div key={i}>
                  <strong>{sent.label}:</strong> {sent.score}
                </div>
              ))
            } 
          />
        ))}
      </div>
      <DisasterChart disasterData={disasterData} />
      <RealTimeUpdates />
    </div>
  );
};

export default Dashboard;

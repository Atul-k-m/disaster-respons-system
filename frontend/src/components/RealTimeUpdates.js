import React, { useEffect, useState } from 'react';
import { initiateSocketConnection, subscribeToUpdates, disconnectSocket } from '../services/socket';

const RealTimeUpdates = () => {
  const [updates, setUpdates] = useState([]);

  useEffect(() => {
    console.log('Initiating socket connection...');
    initiateSocketConnection();

    subscribeToUpdates((update) => {
      console.log('Received update:', update);
      setUpdates(prevUpdates => [update, ...prevUpdates]);
    });

    return () => {
      console.log('Disconnecting socket...');
      disconnectSocket();
    };
  }, []);

  return (
    <div>
      <h2>Real-Time Updates</h2>
      <ul>
        {updates.map((update, index) => (
          <li key={index}>{update.text}</li>
        ))}
      </ul>
    </div>
  );
};

export default RealTimeUpdates;
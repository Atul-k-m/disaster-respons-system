import React, { useEffect, useState } from 'react';
import { initiateSocketConnection, subscribeToUpdates, disconnectSocket } from '../services/socket';

const RealTimeUpdates = () => {
  const [updates, setUpdates] = useState([]);

  useEffect(() => {
    initiateSocketConnection();
    subscribeToUpdates((update) => {
      setUpdates(prevUpdates => [update, ...prevUpdates]);
    });

    return () => disconnectSocket();
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

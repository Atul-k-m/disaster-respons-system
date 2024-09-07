import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

const DisasterChart = ({ disasterData }) => {
  const categories = ['Flood', 'Earthquake', 'Wildfire', 'Hurricane', 'Pandemic', 'Funny'];
  const dataToProcess = Array.isArray(disasterData) ? disasterData : [];
  const counts = categories.map(category => {
    const count = dataToProcess.filter(item => item.category.toLowerCase() === category.toLowerCase()).length;
    console.log(`Count for ${category}: ${count}`);
    return count;
  });

  const data = {
    labels: categories,
    datasets: [{
      label: 'Disaster Categories',
      data: counts,
      backgroundColor: [
        'rgba(75, 192, 192, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 99, 132, 0.2)',
        'rgba(255, 159, 64, 0.2)'
      ],
      borderColor: [
        'rgba(75, 192, 192, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 99, 132, 1)',
        'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1,
    }]
  };

  ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

  console.log('Data:', data);
  return (
    <div>
      <h2>Disaster Overview</h2>
      <Bar data={data} />
    </div>
  );
};

export default DisasterChart;
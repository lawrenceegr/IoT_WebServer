import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('/api/data')
      .then(response => setData(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      {data.map(document => (
        <div key={document._id}>
          <p>Humidity: {document.humidity}</p>
          <p>Temperature: {document.temperature}</p>
          <p>Wind Speed: {document.wind_speed}</p>
          <p>Date: {document.date}</p>
        </div>
      ))}
    </div>
  );
}

export default App;

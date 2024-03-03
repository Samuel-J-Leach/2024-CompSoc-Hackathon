import React from 'react';
import Layout from '/pages/layout.jsx';
import {useEffect, useState} from 'react';
import axios from 'axios';

function HomePage() {
  //const endpoint = 'http://localhost:8000/Student';
  //const fetchData = async() => {
  //  console.log("fetching data...")
  //  const response = await axios.get(endpoint)
  //  console.log(response)
  //  const {data} = response
  //  console.log(data)
  //  return data
  //}
  //useEffect(() => {
  //  fetchData()
  //}, [])

  const [data, setData] = useState([]);
  const [newItem, setNewItem] = useState('');
  // FETCHING DATA TO DISPLAY
  useEffect(() => {
    fetch('http://localhost:8000/Student/',{credentials:'include'})
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  // POSTING DATA
  const handlePostData = async () => {
    try {
      const response = await fetch('http://localhost:8000/Student/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: newItem }),
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const newData = await response.json();
      setData(newData);
    } catch (error) {
      console.error('Error posting data:', error);
    }
  };

  return (
    <app>
        <Layout> 
        <div class="heading-box">
          <h1 className='headings'>STUDENT VIEW</h1>
        </div>
        <div class = "dashboard">
            mhm
        </div>
        <input 
          type = "text" 
          value = {newItem} 
          onChange={(e) => setNewItem(e.target.value)} />
        <button onClick = {handlePostData}> Post Data</button>
        <ul>
          {data.map(el => <li key={el.id}>{el.URN} - {el.FName} {el.LName} - {el.COURSE} - {el.preference}</li>)}
        </ul>
        </Layout>
    </app>
  );
}

export default HomePage;
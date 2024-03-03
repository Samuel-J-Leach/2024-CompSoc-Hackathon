import React from 'react';
import {useEffect, useState} from 'react';
import Layout from './layout';
import TextBox from '/components/textIntBox.jsx';
import {useRouter} from 'next/router';

function studentMark() {

  const [data, setData] = useState([]);
  const [newItem, setNewItem] = useState('');9
  // FETCHING DATA TO DISPLAY
  useEffect(() => {
    fetch('http://localhost:8000/StudentMark/',{credentials:'include'})
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

    const router = useRouter();
    const { query } = router;
    const MARK_ID = query.MARK_ID;

    

    async function patchMark (MARK_ID, selectedMark) {
        try {
          const response = await fetch(`http://localhost:8000/markPatch-endpoint/`, {
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ "MARK_ID": MARK_ID, "Mark": parseFloat(selectedMark) }),
            //body: JSON.stringify({ "MARK_ID": "2345156" , "preference": "web development" }),
          });
    
          if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
          }
      
          const updatedData = await response.json();
          console.log('Preference updated:', updatedData);
        } catch (error) {
          console.error('Error updating preference:', error.message);
        }
      };

  // Possible mark validation later
  const markValidation = (value) => {
    if(!value) {
        return "MARK_ID is required.";
    } else if (!regularexp.test(value)) {
        return "MARK_ID is invalid.";
    } else {
        return "";
    }
};

  return (
    <app>
    <Layout>
      <div class="body-box">
        <div class="heading-box">
          <h1 className='headings'>Change Mark</h1>
        </div>
        <div class = "dashboard">
          <div class="static-card-link">
              <TextBox
                  placeholderText="enter Mark..."
                  labelText="Enter Student Mark for this assessment:"
                  onChange={(e) => {
                    setNewItem(e.target.value);
                    setMarkError(''); 
                  }}
              />
               
          </div>
          <p> {MARK_ID} </p>
          <button onClick={() =>patchMark({MARK_ID}, newItem)}>
            Submit Marks
        </button>
        </div>
      </div>
    </Layout>
</app>
);
}

export default studentMark;
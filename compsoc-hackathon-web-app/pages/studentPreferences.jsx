import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import Layout from '/pages/layout.jsx';
import TextBox from '/components/textBox.jsx';
import DropDown from '/components/dropDown.jsx';

function preferencesPage() {
    const router = useRouter();
    const { query } = router;
    const urn = query.urn;

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

    const urnValidation = (value) => {
        const regularexp = /\d{7}/;
        if(!value) {
            return "URN is required.";
        } else if (!regularexp.test(value)) {
            return "URN is invalid.";
        } else {
            return "";
        }
    };

    const nameValidation = (value) => {
        const regularexp = /[A-Z][a-z]{0,9}/;
        if(!value) {
            return "Name is required.";
        } else if (!regularexp.test(value)) {
            return "Name is invalid.";
        } else {
            return "";
        }
    };

    const [selectedOption, setSelectedOption] = useState(null);
    const handleDropDownChange = (event) => {
        setSelectedOption(event.target.value);
        console.log(event.target.value);
    }; 

    
                /*
                <div class="static-card-link">
                    <TextBox
                        placeholderText="enter forename..."
                        labelText="Enter Name:"
                        validation={nameValidation}
                    />
                    <TextBox
                        placeholderText="enter surname..."
                        validation={nameValidation}
                    />
                </div>
                */
    return (
      <app>
          <Layout>
            <div class="body-box">
              <div class="heading-box">
                <h1 className='headings'>Choose Student Preferences</h1>
              </div>
              <div class = "dashboard">
                <div class="static-card-link">
                    <TextBox
                        placeholderText="enter urn..."
                        labelText="Enter URN:"
                        validation={urnValidation}
                    />
                </div>
                <div class="preference-card">
                    <DropDown urn = {urn}
                        onUpdatePreference={(selectedURN, selectedPreference) => {
                            // Call the function to update the preference on the backend
                            updateStudentPreference(selectedURN, selectedPreference);}}
                    />
                </div>
              </div>
            </div>
          </Layout>
      </app>
    );
  }
  
  export default preferencesPage;
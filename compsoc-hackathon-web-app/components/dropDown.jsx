import React, { useState, useEffect } from 'react';

/*DATA IS NOT PASSED AS AN ENUM WHICH IS WHY IT DOESNT WORK... CHECK MODELS.
const Dropdown = ({ fetchDataUrl, onChange }) => {
  const [options, setOptions] = useState([]);

  useEffect(() => {
    fetch(fetchDataUrl, { credentials: 'include' })
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        return response.json();
      })
      .then(data => {
        // Convert enum object to array of objects
        const optionsArray = Object.keys(data).map(key => ({
          id: key,
          name: data[key]
        }));
        setOptions(optionsArray);
      })
      .catch(error => console.error('Error fetching data:', error));
  }, [fetchDataUrl]);

  return (
    <select onChange={onChange}>
      {options.map(option => (
        <option key={option.id} value={option.id}>{option.name}</option>
      ))}
    </select>
  );
};
*/

const DropDown = ({urn}) => {
  var [preferences, setPreferences] = useState([]);
  var [selectedPreference, setSelectedPreference] = useState('');
  // Function 1
  useEffect(() => {
      const fetchData = async () => {
          try {
              const response = await fetch('http://localhost:8000/api/preferences/');
              setPreferences((await response.json()).preferences);
          } catch (error) {
              console.error('Error fetching preferences:', error);
          }
      };

      fetchData();
  }, []);

  //const postPreference = async (urn, selectedPreference) => {
  async function postPreference (urn, selectedPreference) {
    try {
      const response = await fetch(`http://localhost:8000/patch-endpoint/`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ "URN": urn, "preference": selectedPreference }),
        //body: JSON.stringify({ "URN": "2345156" , "preference": "web development" }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
      }
  
      const updatedData = await response.json();
      console.log('Preference updated:', updatedData);
    } catch (error) {
      console.log(urn);
      console.error('Error updating preference:', error.message);
    }
  };

  // Possible mark validatio
  const markValidation = (value) => {
    if(!value) {
        return "URN is required.";
    } else if (!regularexp.test(value)) {
        return "URN is invalid.";
    } else {
        return "";
    }
};

  return (
    <div>
            <h2>Student Preferences</h2>
            <label htmlFor="preferencesDropdown"></label>
            <select id="preferencesDropdown"
            value = {selectedPreference}
            onChange={(e) => setSelectedPreference(preferences[e.target.value])}>
                <option value="">Select...</option>
                {/* Maps object Preferences */}
                {Object.entries(preferences).map(([key, value]) => (
                  <option key={key} value={value}>
                    {value}
                  </option>
                ))}
            </select>
            <button onClick={() => postPreference(urn, selectedPreference)}> Update </button>
    </div>
  );
};

export default DropDown;


import React, { useState, useEffect } from 'react';

const DropDown = ({ apiUrl }) => {
  const [preferences, setPreferences] = useState({});
  const [selectedPreference, setSelectedPreference] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        setPreferences(data.preferences || {}); // Ensure preferences is an object
      } catch (error) {
        console.error('Error fetching preferences:', error);
      }
    };

    fetchData();
  }, [apiUrl]);

  const postPreference = async () => {
    try {
      const response = await fetch(apiUrl, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ preference: selectedPreference }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const updatedData = await response.json();
      console.log('Preference updated:', updatedData);
    } catch (error) {
      console.error('Error updating preference:', error.message);
    }
  };

  return (
    <div>
      <h2>Student Preferences</h2>
      <label htmlFor="preferencesDropdown">Select Preference:</label>
      <select
        id="preferencesDropdown"
        value={selectedPreference}
        onChange={(e) => setSelectedPreference(e.target.value)}
      >
        <option value="">Select...</option>
        {Object.entries(preferences).map(([key, value]) => (
          <option key={key} value={key}>
            {value}
          </option>
        ))}
      </select>
      <button onClick={postPreference}>Update</button>
    </div>
  );
};

export default DropDown;

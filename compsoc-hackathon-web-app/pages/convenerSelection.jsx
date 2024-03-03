import React, { useState, useEffect } from 'react';
import Layout from '/pages/layout.jsx';
import DropDown from '/components/dropDownGeneric.jsx';

function HomePage() {
    const [selectedOption, setSelectedOption] = useState(null);
    const handleDropDownChange = (event) => {
        setSelectedOption(event.target.value);
    }; 

    return (
    <app>
        <Layout>
          <div class="body-box">
            <div class="heading-box">
                <h1 className='headings'>Allocate Academics to Student</h1>
            </div>
            <div class = "dashboard">
                <div class="preference-card">
                    <DropDown
                        apiUrl="http://localhost:8000/api/StudentURN"
                        onChange={handleDropDownChange}
                    />
                </div>
            </div>
          </div>
        </Layout>
    </app>
  );
}

export default HomePage;
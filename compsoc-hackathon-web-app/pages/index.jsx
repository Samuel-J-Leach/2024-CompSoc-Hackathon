import React from 'react';
import Layout from '/pages/layout.jsx';

function HomePage() {
  return (
    <app>
        <Layout>
          <div class="body-box">
            <div class="heading-box">
              <h1 className='headings'>Choose User</h1>
            </div>
            <div class = "dashboard">
              <a class = "card-link" href= "/studentPreferences"> 
                <h2 class= "card">Student</h2>
              </a>
              <a class="card-link" href="/chooseModule">
                <h2 class= "card">Convener</h2>
              </a>
              <a class = "card-link" href= "/academicLogin"> 
                <h2 class= "card">Academic</h2>
              </a>
            </div>
          </div>
        </Layout>
    </app>
  );
}

export default HomePage;
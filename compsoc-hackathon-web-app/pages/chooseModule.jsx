import React from 'react';
import Layout from '/pages/layout.jsx';

function HomePage() {
  return (
    <app>
        <Layout>
          <div class="body-box">
            <div class="heading-box">
              <h1 className='headings'>Module Selection</h1>
            </div>
            <div class = "dashboard">
              <a class = "card-link" href= "/convenerSelection"> 
                <h2 class= "card"> COM1026</h2>
              </a>
              <a class="card-link" href = "/convenerSelection">
                <h2 class= "card"> COM1027</h2>
              </a>
              <a class = "card-link" href= "/convenerSelection"> 
                <h2 class= "card"> COM1028</h2>
              </a>
              <a class="card-link" href = "/convenerSelection">
                <h2 class= "card"> COM1030</h2>
              </a>
              <a class="card-link" href = "/convenerSelection">
                <h2 class= "card"> COM1031</h2>
              </a>
            </div>
          </div>
        </Layout>
    </app>
  );
}

export default HomePage;
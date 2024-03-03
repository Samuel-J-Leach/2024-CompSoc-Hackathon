import React from 'react';
import Layout from '/pages/layout.jsx';
import DataTable from './academicTable';
import { useRouter } from 'next/router'

function HomePage() {
  const router = useRouter()
  return (
    <app>
      <p>Post: {router.query.slug}</p>
        <Layout> 
        <div class="heading-box">
          <h1 className='headings'>ACADEMIC VIEW</h1>
        </div>
        <DataTable />
        </Layout>
    </app>
  );
}

export default HomePage;
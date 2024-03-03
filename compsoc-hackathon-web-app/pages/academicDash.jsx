// pages/academicDash.js
import { useRouter } from 'next/router';
import Layout from './layout';
import DataTable from './academicTable';


const AcademicDashPage = () => {
  const router = useRouter();
  const { query } = router;
  const urn = query.urn;

  return (
    <Layout>
      <div className="body-box">
        <div className="heading-box">
          <h1 className="headings">Academic Dashboard</h1>
        </div>
        <div className="heading-box">
          <h2 className="subheadings">User URN: {urn}</h2>
        </div>
        <div className="user-details">
          
          {/* Add more dynamic content based on the URN */}
          <DataTable urn = {urn} />
        {/* For DataTable, make sure to only show students who belong to the academic 
            Then ensure each student row links to a "assessments page" showing their list of assessments
        */}

        </div>
      </div>
    </Layout>
  );
};

export default AcademicDashPage;
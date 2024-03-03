// components/DataTable.js
import { useEffect, useState } from 'react';

const DataTable = ({urn}) => {
  const [studentData, setStudentData] = useState([]);
  const [studentMarkData, setStudentMarkData] = useState([]);
  
  useEffect(() => {
    fetch('http://localhost:8000/Student/',{credentials:'include'})
      .then(response => response.json())
      .then(studentData => setStudentData(studentData))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  useEffect(() => {
    fetch('http://localhost:8000/StudentMark/',{credentials:'include'})
      .then(response => response.json())
      .then(studentMarkData => setStudentMarkData(studentMarkData))
      .catch(error => console.error('Error fetching data:', error));
  }, []);
  //console.log(urn);
  //const joe = data.filter(el => {if (el.URN == {urn}) return el;})
  //  .catch(error => console.error('empty table:', error));
  //above code will show an error if there is no data in the requested table
  //hallam gives head for urban outfitters vouchers

  //const filteredStudentMarkData = studentMarkData.filter( el =>{if(el.ACADEMIC == {urn}) return el;});
  //console.log('Filtered Student Mark Data:', filteredStudentMarkData);

  return (
    <div class="container">
      <h2>Data Table for {urn}</h2>
      <p> URN - Name - Assessment - Mark </p>
      --------------------------------
      <div>
        {studentMarkData.filter( mark =>{if(mark.ACADEMIC == urn) return mark;}).map(mark => (
          <div key={mark.MARK_ID}>
            {studentData.filter(student => {if (student.URN == mark.STUDENT) return student}).map(student => (
              <a href={`/studentAssessment?MARK_ID=${encodeURIComponent(mark.MARK_ID)}`}> {student.URN} - {student.FName} {student.LName} - {mark.ASSESSMENT} - {mark.Mark} </a>
            ))}
          </div>
        ))}
      </div>
      <br></br>
      <br></br>
      <br></br>
    </div>
  );
};

export default DataTable;

/*
<table class = "data-table">
        <thead>
          <tr>
            <th>URN</th>
            <th>Name</th>
            <th> Assessment </th>
            <th> Mark </th>
          </tr>
        </thead>
        <tbody>
          {studentMarkData.filter( mark =>{if(mark.ACADEMIC == urn) return mark;}).map(mark => (
            <tr key={mark.MARK_ID}>
              <td> {mark.STUDENT} </td>
              <td></td>
              <td>  </td>
              <td> {mark.Mark} </td>
            </tr>
          ))}
        </tbody>
      </table>
*/
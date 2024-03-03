import Layout from '/pages/layout.jsx';
import TextBox from '/components/textBox.jsx';
import {useEffect, useState} from 'react';

function HomePage() {
  const [data, setData] = useState([]);
  const [newItem, setNewItem] = useState('');
  // FETCHING DATA TO DISPLAY
  useEffect(() => {
    fetch('http://localhost:8000/Academic/',{credentials:'include'})
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  // POSTING DATA
  const handlePostData = async () => {
    try {
      const response = await fetch('http://localhost:8000/Academic/', {
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

  
    const [urn, setUrn] = useState('');
    const [password, setPassword] = useState('');
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      
      if (!urn || !password) {
        console.error('URN and password are required');
        return;
      }

      console.log('URN:', urn);
      console.log('Password:', password);
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
  return (
    <app>
        <Layout>
          <div class="body-box">
            <div class="heading-box">
              <h1 className='headings'>Academic Login</h1>
            </div>
            <div class = "dashboard">
            {data.map(el => (
          <a key={el.URN} className="card-link" href={`/academicDash?urn=${encodeURIComponent(el.URN)}`}>
            <h2 className="card">({el.URN}) {el.FName} {el.LName}</h2>
          </a>
        ))}
            </div>
          </div>
        </Layout>
    </app>
  );
}

export default HomePage;
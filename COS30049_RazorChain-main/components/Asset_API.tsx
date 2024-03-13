import axios from 'axios';
import React, {useState,useEffect } from 'react';


export function RZCtoken() {
    const [userData, setUserData] = useState(null);
  
    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await axios.get('http://localhost:8000/assets');
          // Assuming the API response is an object with a single property 'value'
          setUserData(response.data.content.data[5].asset_symbol);
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };

      fetchData();
    }, []);

    return(<span> {userData !== null ? ( <span>{userData}</span> ) : ( <p>Loading...</p>)} </span>);
}  

export function RZCsupply() {
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/assets');
        // Assuming the API response is an object with a single property 'value'
        setUserData(response.data.content.data[5].total_supply);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return(<span> {userData !== null ? ( <span>{userData}</span>) : ( <p>Loading...</p>)} </span>);
}  

export function SCItoken() {
  const [userData, setUserData] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/assets');
        // Assuming the API response is an object with a single property 'value'
        setUserData(response.data.content.data[6].asset_symbol);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return(<span> {userData !== null ? ( <span>{userData}</span> ) : ( <p>Loading...</p>)} </span>);
}  

export function SCIsupply() {
const [userid, setuserid] = useState(null);

useEffect(() => {
  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:8000/assets');
      // Assuming the API response is an object with a single property 'value'
      setuserid(response.data.content.data[6].total_supply);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  fetchData();
}, []);

return(<span> {userid !== null ? ( <span>{userid}</span>) : ( <p>Loading...</p>)} </span>);
}  

export function UserAddress() {
  const [useraddress, setuseraddress] = useState();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/users/1');
        // Assuming the API response is an object with a single property 'value'
        setuseraddress(response.data.content.userDetail.wallet_add);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return(<span> {useraddress !== null ? ( <span>{useraddress}</span>) : ( <p>Loading...</p>)} </span>);
}  

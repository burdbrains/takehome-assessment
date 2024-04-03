import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [doctors, setDoctors] = useState([]);

  const [current_doctor, setCurrentDoctor] = useState("No Doctor Selected");

  const handleSelect = (doctor_id, doctor_name) => {
    setCurrentDoctor(doctor_name)
    populateSimilarDoctors(doctor_id)
  }

  const populateSimilarDoctors = async (doctor_id) => {
    const response = await fetch(`http://127.0.0.1:8000/retrieve-similar-doctors?doctor_id=${doctor_id}`, {
      method: 'GET', // Specify GET method
      headers: {
        'Content-Type': 'application/json', // Optional header for JSON data (if applicable)
        'doctor_id': doctor_id // Include the doctor_id in the header
      }
    });

    const data = await response.json();
    setDoctors(data.doctors)
  }

  const populateList = () => {
    fetch('http://127.0.0.1:8000/retrieve-doctors')
    .then(
      res => res.json()
    )
    .then(
      data => {
        setDoctors(data.doctors)
        console.log(data)
      }
    )
  }

  useEffect(() => {
    populateList();
  }, []);

  return (
    <>
      <div className="card">
      <p className="read-the-docs">
        {current_doctor}
      </p>
        {doctors.map((doctor, index) => (
          <div className="doctor-list-container">
            <ul className="doctor-list">
              <li key={index}>
                <button onClick={() => handleSelect(doctor.id, doctor.name)}>Select</button>
                {doctor.name} - {doctor.specialty} - {doctor.zipcode} - {doctor.rating}/5 - {doctor.experience} years
              </li>
            </ul>
          </div>
        ))}
      </div>
    </>
  )
}

export default App

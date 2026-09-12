import { useEffect, useState } from 'react'

function App() {
  const [message, setMessage] = useState('Loading...')

  useEffect(() => {
    fetch('http://127.0.0.1:8000/')
      .then(response => response.json())
      .then(data => setMessage(data.message))
  }, [])

  return (
    <div>
      <h1>Smart Waste Bin</h1>
      <p>{message}</p>
    </div>
  )
}

export default App
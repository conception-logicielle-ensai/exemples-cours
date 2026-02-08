import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <img src="https://kinsta.com/fr/wp-content/uploads/sites/4/2019/01/qu-est-ce-que-nginx.png" />
      </div>
      <h1>Image light qui tourne sur un nginx a partir de ce qui a été construit côté VITE/React</h1>
    </>
  )
}

export default App

import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [products, setProducts] = useState([])
  useEffect(()=>{
    fetchData();

  },[])

  const fetchData=async()=>{
    const response = await fetch("http://127.0.0.1:8000/api/acc/store/products/")
    const data = await response.json()
    console.log(data)
    setProducts(data)

  }

  return (
    <>
      <div className='bg-gray-900'>
        <nav className='bg-gray-900 flex justify-around text-white w-100 h-12 pt-4'>
          <nav className='flex'><h2>gembay</h2>
          
          
          </nav>
          
          <nav>
            <ul className='flex gap-4'>
              <li>home</li>
              <li>products</li>
              <li>about</li>
            </ul>
          </nav>
          <nav className='flex gap-4 border-r-4'>
            <button className='bg-yellow-600'>sign in </button>
            <button className='bg-green-600'>cart</button>
          </nav>
        </nav>
        <div></div>
        <div className='bg-slate-500'><h1><b>products</b></h1>
          <div className='flex flex-wrap gap-8 ml-12'>

            {products.map((product)=>(

              <div className='w-64 h-64 bg-yellow-100'>

                <img src={`http://127.0.0.1:8000/${product.pimage}`} 
                alt=""
                className='w-full h-40 object-cover' />
                name:{product.pname} <br />
                price:{product.pprice} <br />
                <div className='flex gap-8'>
                <button className='bg-green-700 w-32 hover:bg-green-400'>add to cart</button>
                <button className='bg-yellow-200 w-28 hover:bg-yellow-400'>view</button></div>
            </div>
            







))}

          </div>
        </div>
   

      </div>
    </>
  )
}

export default App

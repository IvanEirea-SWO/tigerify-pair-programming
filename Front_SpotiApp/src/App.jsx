import { useState } from 'react'
import Button from './components/Button'
import Table from './components/Table'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <>
        <h1>SpotiMock</h1>
      </>
      <>
        <Button name='submit'></Button>
        <Table name='songs'></Table>
      </>
    </>
  )
}

export default App

import React, { useState, useEffect } from 'react';
import Sidebar from './components/Sidebar';
import Chat from './components/Chat';

const App = () => {
  const [value, setValue] = useState('')
  const [message, setMessage] = useState('')
  const [previousChats, setPreviousChats] = useState([])
  const [currentTitle, setCurrentTitle] = useState(null)

  const createNewChat = () => {
    setMessage('')
    setValue('')
    setCurrentTitle(null)
  }

  const handleClick = (uniqueTitle) => {
    setCurrentTitle(uniqueTitle)
    setMessage('')
    setValue('')
  }

  const getMessages = async (e) => {
    e.preventDefault()
    const options = {
        method: "POST",
        body: JSON.stringify({
            message: value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }
    try {
        const response = await fetch('http://localhost:8000/completions', options)
        const data = await response.json()
        // console.log(data)
        setMessage(data.choices[0].message)
    } catch (error) {
        console.error(error)
    }
      // setValue('');
  }
  // console.log(message)

  useEffect(() => {
    console.log(currentTitle, value, message)
    if (!currentTitle && value && message) {
        setCurrentTitle(value)
    }
    if (currentTitle && value && message) {
        setPreviousChats(prevChats => (
            [...prevChats,
            {
                title: currentTitle,
                role: 'user',
                content: value
            },
            {
                title: currentTitle,
                role: message.role,
                content: message.content
            }]
        ))
    }
  }, [message, currentTitle])

  console.log(previousChats)

  const currentChat = previousChats.filter(previousChat => previousChat.title === currentTitle)
  const uniqueTitles = Array.from(new Set(previousChats.map(previousChat => previousChat.title)))
  console.log(uniqueTitles)

  return (
    <div className="app">
        <Sidebar uniqueTitles={uniqueTitles} createNewChat={createNewChat} handleClick={handleClick} />
        <Chat currentChat={currentChat} value={value} getMessages={getMessages} setValue={setValue} />
    </div>
  );
}

export default App;

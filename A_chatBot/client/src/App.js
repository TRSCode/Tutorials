import { useState, useEffect } from 'react';

const App = () => {
  const[value, setValue] = useState('')
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
      <section className="side-bar" >
        <button onClick={createNewChat} >+ New chat</button>
        <ul className="history" >
          {uniqueTitles?.map((uniqueTitle, index) => <li key={index} onClick={() => handleClick(uniqueTitle)} >{uniqueTitle}</li>)}
        </ul>
        <nav>
          <p>Made by Tony</p>
        </nav>
      </section>
      <section className="main" >
        {!currentTitle && <h1>tonyGPT</h1>}
        <ul className="feed">
          {currentChat?.map((chatMessage, index)=> 
          <li key={index}>
            <p className="role" >{chatMessage.role}</p>
            <p>{chatMessage.content}</p>
          </li>)}
        </ul>
        <div className="bottom-section">
          <form onSubmit={getMessages} className="input-container"> {/* Added form element */}
            <input value={value} onChange={(e) => setValue(e.target.value)} />
            <div id="submit" onClick={getMessages}>➢</div>
          </form> {/* Close form element */}
          {/* <div className="input-container">
            <input value={value} onChange={(e) => setValue(e.target.value)} />
            <div id="submit" onClick={getMessages}>➢</div>
          </div> */}
          <p className="info">
            Chat GPT Mar 14 Version.  Free Research Preview.
            Our goal is to make AI systems more natural and safe to interact with.
            Your feedback will help us improve.
          </p>
        </div>
      </section>
    </div>
  );
}

export default App;

import React from 'react';

const Chat = ({ currentChat, value, getMessages, setValue }) => {
    return (
        <section className="main">
            {!currentChat.length && <h1>tonyGPT</h1>}
            <ul className="feed">
                {currentChat.map((chatMessage, index) => (
                    <li key={index}>
                        <p className="role">{chatMessage.role}</p>
                        <p>{chatMessage.content}</p>
                    </li>
                ))}
            </ul>
            <div className="bottom-section">
                <form onSubmit={getMessages} className="input-container">
                    <input value={value} onChange={(e) => setValue(e.target.value)} />
                    <div id="submit" onClick={getMessages}>
                        ➢
                    </div>
                </form>
                <p className="info">
                    Chat GPT Mar 14 Version. Free Research Preview. Our goal is to make
                    AI systems more natural and safe to interact with. Your feedback will
                    help us improve.
                </p>
            </div>
        </section>
    );
}

export default Chat;

import React from 'react';
import { ChatList } from './ChatList';
import { InputSection } from './InputSection';

export const ChatWindow = ({ currentTitle, currentChat, value, setValue, getMessages }) => {
    return (
        <section className="main">
            {!currentTitle && <h1>tonyGPT</h1>}
            <ChatList currentChat={currentChat} />
            <InputSection
                value={value}
                setValue={setValue}
                getMessages={getMessages}
            />
        </section>
    );
};


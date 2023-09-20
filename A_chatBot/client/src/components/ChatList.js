import React from 'react';

export const ChatList = ({ currentChat }) => {
    return (
        <ul className="feed">
            {currentChat?.map((chatMessage, index) => (
                <li key={index}>
                    <p className="role">{chatMessage.role}</p>
                    <p>{chatMessage.content}</p>
                </li>
            ))}
        </ul>
    );
};


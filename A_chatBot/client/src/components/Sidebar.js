export const Sidebar = ({ uniqueTitles, createNewChat, handleClick }) => {
    return (
        <section className="side-bar">
            <button onClick={createNewChat}>+ New chat</button>
            <ul className="history">
                {uniqueTitles?.map((uniqueTitle, index) => (
                    <li key={index} onClick={() => handleClick(uniqueTitle)}>
                        {uniqueTitle}
                    </li>
                ))}
            </ul>
            <nav>
                <p>Made by Tony</p>
            </nav>
        </section>
    );
};

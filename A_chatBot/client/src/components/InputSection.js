// import React from 'react';

// export const InputSection = ({ value, setValue, getMessages }) => {
//     return (
//         <div className="bottom-section">
//             <form onSubmit={getMessages} className="input-container">
//                 <input
//                     value={value}
//                     onChange={(e) => setValue(e.target.value)}
//                 />
//                 <div id="submit" onClick={getMessages}>➢</div>
//             </form>
//             <p className="info">
//                 Chat GPT Mar 14 Version. Free Research Preview.
//                 Our goal is to make AI systems more natural and safe to interact with.
//                 Your feedback will help us improve.
//             </p>
//         </div>
//     );
// };
// import React from 'react';

// const InputSection = ({ value, setValue, getMessages }) => {
//     return (
//         <div className="bottom-section">
//             <form onSubmit={getMessages} className="input-container">
//                 <input
//                     value={value}
//                     onChange={(e) => setValue(e.target.value)}
//                 />
//                 <button id="submit" type="submit">➢</button>  {/* Change the div to a button and specify the type */}
//             </form>
//             <p className="info">
//                 Chat GPT Mar 14 Version. Free Research Preview.
//                 Our goal is to make AI systems more natural and safe to interact with.
//                 Your feedback will help us improve.
//             </p>
//         </div>
//     );
// };

// export default InputSection;

import React from 'react';

const InputSection = ({ value, setValue, getMessages }) => {
    return (
        <div className="bottom-section">
            <form onSubmit={getMessages} className="input-container">
                <input
                    value={value}
                    onChange={(e) => setValue(e.target.value)}
                />
                <button id="submit" type="submit">➢</button>  {/* Change the div to a button and specify the type */}
            </form>
            <p className="info">
                Chat GPT Mar 14 Version. Free Research Preview.
                Our goal is to make AI systems more natural and safe to interact with.
                Your feedback will help us improve.
            </p>
        </div>
    );
};

export default InputSection;

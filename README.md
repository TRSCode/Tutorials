## Tutorial Code Along and Other Training

- v3 to v4 Migration Guide
    - https://github.com/openai/openai-node/discussions/217

- __chatBot__: chatGPT chatbot with React & OpenAI (v3)
    - https://www.youtube.com/watch?v=rZWikA35I3I
    - react bootstrap
    
- ** __app__ : chatGPT chatBot#2 called "app" ***(v4)***
    - https://www.youtube.com/watch?v=Lag9Pj_33hM
    - https://github.com/coopercodes/ReactChatGPTChatbot
    - npm create vite@latest app -- --template reacty
    - npm install @chatscope/chat-ui-kit-react
    - ***npm run dev***
    - this is a front-end only chatBot (less secure even with .env)
    
- __fullstack_chatBot__ (v3)
    - https://www.youtube.com/watch?v=OJ7AgZVH118&list=PLOvIwkWvHysNRNjLPcHHAWXrLzRkl__kR&index=4
    - https://github.com/EBEREGIT/react-nodejs-chatgpt-tutorial
    - React/Node.js/Vite

- __A_chatBot__ ***(v4)***
    - https://www.youtube.com/watch?v=JJ9fkYX7q4A
    - frontend and backend in client folder
        - npm run start:frontend
        - npm run start:backend or nodemon server.js
            - see package.json

- __fastAPI_platform_tutorial__ 
    - using the tutorial from fastAPI docs
    - https://fastapi.tiangolo.com/tutorial/ 
    - https://docs.pydantic.dev/latest/
    - 
- __FastAPI_Complete_Course__
    - https://www.udemy.com/course/fastapi-the-complete-course/learn/lecture/36882688?start=15#overview
    - source code for the FastAPI Complete Course on Udemy
- __FastAPI__
    - activate env --> fastapienv\Scripts\activate.bat
        - pip install fastapi 
        - pip install "uvicorn[standard]"
        - pip list
    - deactivate env --> deactivate
    - using sqlite3: (done initially to create the db, doesn't need to run all the time)
        - in terminal type with venv running and cd into the correct folder: sqlite3 todos.db
        - .schema  will show the colums in the db
        - .help 
        - create
            - insert into todos (title, description, priority, complete) values ('Go to the store', 'Pick up eggs', 5, False);
            - insert into todos (title, description, priority, complete) values ('Cut the lawn', 'Grass is getting long', 3, False);
            - insert into todos (title, description, priority, complete) values ('Feed the dog', 'He is getting hungry', 5, False);
            - insert into todos (title, description, priority, complete) values ('Test element', 'Pick up eggs', 5, False);
        - read all
            - select * from todos;
        - change view with .mode column/markdown/box/table etc
        - delete
            - delete from todos where id = 4;
    - bcrypt --> pip install "passLib[bcrypt]"
    
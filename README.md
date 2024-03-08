# Table of Contents <a name="table-of-contents"></a>
1. [Tutorial Code Along and Other Training](#tutorial-code-along-and-other-training)
    - [v3 to v4 Migration Guide](#v3-to-v4-migration-guide)
    - [chatBot: chatGPT chatbot with React & OpenAI (v3)](#chatbot-chatgpt-chatbot-with-react--openai-v3)
    - [app: chatGPT chatBot#2 called "app" (v4)](#app-chatgpt-chatbot2-called-app-v4)
    - [Django Demo Series (Coding Dojo)](#django-demo-series-coding-dojo)
    - [fullstack_chatBot (v3)](#fullstack_chatbot-v3)
    - [A_chatBot (v4)](#a_chatbot-v4)
    - [fastAPI_platform_tutorial](#fastapi_platform_tutorial)
    - [FastAPI Complete Course](#fastapi_complete_course)
    - [FastAPI](#fastapi)
    - [RachelChat](#rachel)
    - [NextJS "NextJS Dasshboard" ](#nextjs_platform_tutorial)
    - [nextJS_Two "nextJS_two" ](#nextjs_two)
    - [nextjs_openai "nextjs_openai" ](#nextjs_openai)

## Tutorial Code Along and Other Training <a name="tutorial-code-along-and-other-training"></a>

- ### v3 to v4 Migration Guide <a name="v3-to-v4-migration-guide"></a>
- [Back to Table of Contents](#table-of-contents)
    - https://github.com/openai/openai-node/discussions/217

- ### chatBot: chatGPT chatbot with React & OpenAI (v3) <a name="chatbot-chatgpt-chatbot-with-react--openai-v3"></a>
- [Back to Table of Contents](#table-of-contents)
    - https://www.youtube.com/watch?v=rZWikA35I3I
    - react bootstrap
    
- ### app: chatGPT chatBot#2 called "app" (v4) <a name="app-chatgpt-chatbot2-called-app-v4"></a>
- [Back to Table of Contents](#table-of-contents)
    - https://www.youtube.com/watch?v=Lag9Pj_33hM
    - https://github.com/coopercodes/ReactChatGPTChatbot
    - npm create vite@latest app -- --template react
    - npm install @chatscope/chat-ui-kit-react
    - npm run dev
    - this is a front-end only chatBot (less secure even with .env)
    
- ### Django Demo Series (Coding Dojo) <a name="django-demo-series-coding-dojo"></a>
- [Back to Table of Contents](#table-of-contents)
    - zoom: https://codingdojo.zoom.us/j/99721516229
    - video: 
    - 

- ### fullstack_chatBot (v3) <a name="fullstack_chatbot-v3"></a>
- [Back to Table of Contents](#table-of-contents)
    - https://www.youtube.com/watch?v=OJ7AgZVH118&list=PLOvIwkWvHysNRNjLPcHHAWXrLzRkl__kR&index=4
    - https://github.com/EBEREGIT/react-nodejs-chatgpt-tutorial
    - React/Node.js/Vite

- ### A_chatBot (v4) <a name="a_chatbot-v4"></a>
- [Back to Table of Contents](#table-of-contents)
    - https://www.youtube.com/watch?v=JJ9fkYX7q4A
    - frontend and backend in client folder
        - npm run start:frontend
        - npm run start:backend or nodemon server.js
            - see package.json

- ### fastAPI_platform_tutorial <a name="fastapi_platform_tutorial"></a>
- [Back to Table of Contents](#table-of-contents)
    - using the tutorial from fastAPI docs
    - https://fastapi.tiangolo.com/tutorial/ 
    - https://docs.pydantic.dev/latest/
    - 

- ### FastAPI Complete Course <a name="fastapi_complete_course"></a>
- [Back to Table of Contents](#table-of-contents)
    - FastAPI, SQLalchemy, SQLite, Alembic, Python, Bootstrap, venv, MySQL, PostgresQL, ElephantQL, Render
    - https://www.udemy.com/course/fastapi-the-complete-course/learn/lecture/36882688?start=15#overview
    - source code for the FastAPI Complete Course on Udemy: https://github.com/codingwithroby/FastAPI-The-Complete-Course/tree/main

- ### FastAPI <a name="fastapi"></a>
- [Back to Table of Contents](#table-of-contents)
    - python -m venv <file_name>
    - activate env --> fastapienv\Scripts\activate.bat
        - pip install fastapi 
        - pip install "uvicorn[standard]"
        - pip list
    - deactivate env --> deactivate
    - using __sqlite3__: (done initially to create the db, doesn't need to run all the time)
        - in terminal type with venv running and cd into the correct folder: sqlite3 todos.db
        - .schema  will show the columns in the db
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
    - python multipart --> pip install python-multipart
    - for jwt --> pip install "python-jose[cryptography]" 
    - Create SECRET_KEY: to print a random list of characters, don't run in venv --> openssl rand -hex 32
    - Test token --> https://jwt.io
    - __PostgreSQL__ https://www.postgresql.org/   
        - launch gui with pgAdmin 4
        - in venv --> pip install psycopg2-binary
    - __MySQL__
        - in venv --> pip install pymysql
    - __Alembic__ is a database migration tool for when using SQLAlchemy
        - pip install alembic
        - initialize alembic project which will create two new files (alembic.ini and alembic directory)
            - alembic init <folder name>  **creates new venv for alembic
            - alembic revision -m <message>  **creates a new revision (write scripts - creates file and ID)
            - alembic upgrade <revision #>   **run our upgrade migration to our database which will be a function inside revision file
            - alembic downgrade -1    **run our downgrade migration to our database
    - project 4
        - in venv --> pip install aiofiles
        - --> pip install jinja2
        - create requirements file
            - navigate to appropriate project folder
            - in terminal --> pip3 freeze > requirements.text
        - Deployment:
            - Render
            - ElephantSQL (using postgresql)
    

- ### RachelChat <a name="rachel"></a>
- [Back to Table of Contents](#table-of-contents)
    - https://www.udemy.com/course/chatgpt-ai-voice-chatbot-build-with-react-and-fast-api-combo/learn/lecture/36950450?start=0#overview
    - React/FastAPI/openAI/ElevenLabs (trscod) Udemy course to create voice ai chatbot
    - Frontend set-up (see discord for source code)
        - yarn create vite .
        - ensure have correnct dependencies as listed in provided package.json, in terminal  --> yarn --exact
        - run frontend to see if installed --> yarn dev
        - set-up tailwind (already installed with dependencies) --> npx tailwindcss init -p
    - 
    - Backend
    - 
    - Currently @4:41 of lesson 40


- ### NextJS_platform_tutorial "NextJS Dasshboard" <a name="nextjs_platform_tutorial"></a>
- [Back to Table of Contents](#table-of-contents)
    - using the tutorial from NextJS docs
    - https://nextjs.org/learn
    - https://vercel.com/ chapter 1 complete
    

- ### nextJS_two "nextJS_two" <a name="nextjs_two"></a>
- [Back to Table of Contents](#table-of-contents)
    - YouTube tutorial
    - https://www.youtube.com/watch?v=ZVnjOPwW4ZA
    - npm run dev


- ### NextJS_OpenAI "nextjs_openai" <a name="nextjs_openai"></a>
- [Back to Table of Contents](#table-of-contents)
    - Udemy Course (nextjs-tutorial, gptgenius, jobify)
    - Udemy: https://www.udemy.com/course/nextjs-open-ai/learn/lecture/41657854#overview
    - GitHub: https://github.com/john-smilga/nextjs-course-openai
    - ***nextjs-tutorial***
    - Demo Vercel: https://nextjs-tutorial-production.vercel.app/
    - Tailwindcss: https://v2.tailwindcss.com/docs
    - DaisyUI: https://daisyui.com/
    - Prisma DB migration/update: npx prisma migrate dev
    - Prisma DB PUSH: npx prisma db push
    - Prisma Run: npx prisma studio
    - Prisma: npx prisma studio
    - Zod (typescript declaration and validation library): https://zod.dev
    - Beautiful Toasts (provides notififactions neatly): https://react-hot-toast.com
    - server actions replaced route handlers, but still may be usefull which allow the creation of serverless functions with less set up. Like Postman in vs code.
        - Thunder Client (a VS Code extension): 
    - Middleware: 
        - https://nextjs.org/docs/app/building-your-application/routing/middleware
    - database web provider Render: https://dashboard.render.com/
    - Deploy on vercel: https://vercel.com/
    - ***gptGenius***
    - Clerk user authentication: https://clerk.com
        - Clerk docs for Next.JS: https://clerk.com/docs/quickstarts/nextjs
    - React-Icons: https://react-icons.github.io/react-icons/
    - DaisyUI component drawer: https://daisyui.com/components/drawer/
    - PlanetScale: https://app.planetscale.com/
    - Unsplash images: https://unsplash.com/
    - axios needed for unsplash api: npm i axios
    - Prisma Schema upate: dont for get to push the schema update: npx prisma db push
    - vercel has a 10 second lag timeout which can effect rendering, see lessons 96 and 103 for discussion and suggestions
    - ***jobify*** (next.js | Shadcn-ui | clerk | Typescript | Render | Prisma | Toast | Stats | Charts | Vercel)
    - install this time with Typescript and eslint
    - initial install loads all dependencies for the project and are specific regarding versions
    - using snippets: ***rfce*** in .tsx vs ***rafce*** in .jsx
    - production app: https://nextjs-jobify-production.vercel.app/
    - shadcn/ui (requires 2 more installs): https://ui.shadcn.com/
    - Lucide React (icon library used by Shadcy): https://lucide.dev/guide/packages/lucide-react
    - Logos/Images/Art (good for matching colors in your Theme)
        - Favicon: https://favicon.io/
        - unDraw: https://undraw.co/
        - Logo - Figma: https://www.figma.com/community
    - Render and Prisma:
        - https://dashboard.render.com/
        - create render db and get external URL(placed in .env)
        - add .env to .gitignore
        - create util/db.ts
        - update prisma/schema.prisma
        - already installed
        - npx prisma init
        - npx prisma db push
        - npx prisma studio
    - Shadcn Toast: npx shadcn-ui@latest add toast
    - add reactQuery to the project
    - mockaroo (create mock data to seed DB): https://mockaroo.com/
    - 
    - complete through lesson 136
- [Back to Table of Contents](#table-of-contents)
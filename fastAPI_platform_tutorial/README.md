A good modular file structure allows for clear separation of concerns, scalability, and maintainability of your FastAPI application. Below is a suggested modular structure for a FastAPI project:

```
/backend or server
|-- /app
|   |-- /api
|   |   |-- /v1
|   |   |   |-- /user
|   |   |   |   |-- __init__.py
|   |   |   |   |-- routes.py
|   |   |   |   |-- models.py
|   |   |   |   |-- schemas.py
|   |   |   |-- /item
|   |   |   |   |-- ...
|   |   |-- __init__.py
|   |-- /core
|   |   |-- config.py
|   |   |-- db.py
|   |   |-- security.py
|   |-- /db
|   |   |-- /migrations
|   |   |-- models.py
|   |   |-- session.py
|   |-- /services
|   |   |-- user_service.py
|   |   |-- item_service.py
|   |   |-- ...
|   |-- /tests
|   |   |-- test_users.py
|   |   |-- ...
|   |-- /main.py
|-- /Dockerfile
|-- /docker-compose.yml
|-- /requirements.txt
|-- /README.md
```

Here's a breakdown:

1. **/app:** This is where your main application resides.
    - **/api:** This directory can contain different versions of your API.
        - **/v1:** Version 1 of your API.
            - **/user:** Each resource or group of routes can have its directory.
                - **routes.py:** FastAPI route definitions.
                - **models.py:** Pydantic models for request and response handling.
                - **schemas.py:** ORM (like SQLAlchemy) schema definitions.
    - **/core:** Core functionalities and configurations.
        - **config.py:** Application-wide configurations.
        - **db.py:** Database-related utilities.
        - **security.py:** Authentication and authorization utilities.
    - **/db:** Database-related files.
        - **/migrations:** For database migrations.
        - **models.py:** ORM model definitions.
        - **session.py:** Database session utilities.
    - **/services:** Business logic. Encapsulating logic here makes the app more testable and modular.
    - **/tests:** Unit and integration tests.

2. **/main.py:** The main file to start the application.

3. **/Dockerfile:** If you're containerizing your app.

4. **/docker-compose.yml:** Useful for local development and defining service dependencies.

5. **/requirements.txt:** Your Python dependencies.

6. **/README.md:** Documentation for your project.

As your application grows, you might need to adjust this structure to fit your needs. For instance, you might introduce a `middlewares`, `exceptions`, or `utils` directory. The key is to keep related functionalities grouped together and have a clear understanding of where to find and place different pieces of your application.
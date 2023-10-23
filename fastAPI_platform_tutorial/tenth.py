from typing import Annotated, Union, List, Any
from fastapi import FastAPI, Path, Query, Body, Cookie, Header, Response, status, Form, File, UploadFile
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Response Status Code, Form Data, Request Files, Request Forms and Files"}

# @app.post("/items/", status_code=status.HTTP_201_CREATED)
# async def create_item(name: str):
#     return {"name": name}

# --- install and import python-multipart  ---

# @app.post("/login/", status_code=201)
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     return {"username": username}

# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}

# --- Request Forms and Files ---

app = FastAPI()


@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
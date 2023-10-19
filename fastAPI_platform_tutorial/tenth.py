from typing import Annotated, Union, List, Any
from fastapi import FastAPI, Path, Query, Body, Cookie, Header, Response, status, Form
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Response Status Code and Form Data"}

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}

# --- install and import python-multipart  ---

@app.post("/login/", status_code=201)
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
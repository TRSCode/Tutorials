from typing import Annotated, Union
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Body - Fields"}
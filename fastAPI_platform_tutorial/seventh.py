from typing import Annotated, Union, List
from fastapi import FastAPI, Path, Query, Body, Cookie
from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Cookie Parameters"}

@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}
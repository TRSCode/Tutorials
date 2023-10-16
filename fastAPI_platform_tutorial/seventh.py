from typing import Annotated, Union, List
from fastapi import FastAPI, Path, Query, Body, Cookie, Header
from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Cookie and Header Parameters"}

# @app.get("/items/")
# async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
#     return {"ads_id": ads_id}

# @app.get("/items/")
# async def read_items(user_agent: Annotated[str | None, Header()] = None):
#     return {"User-Agent": user_agent}

# @app.get("/items/")
# async def read_items(
#     strange_header: Annotated[str | None, Header(convert_underscores=False)] = None
# ):
#     return {"strange_header": strange_header}

@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}
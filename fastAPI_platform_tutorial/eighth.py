from typing import Annotated, Union, List, Any
from fastapi import FastAPI, Path, Query, Body, Cookie, Header, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Response Model - Return Type"}

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []


# @app.post("/items/")
# async def create_item(item: Item) -> Item:
#     return item


# @app.get("/items/")
# async def read_items() -> list[Item]:
#     return [
#         Item(name="Portal Gun", price=42.0),
#         Item(name="Plumbus", price=32.0),
#     ]

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr # need to install email-validator: pip install email-validator
#     full_name: str | None = None


# # Don't do this in production! Never store the plain password of a user or send it in a response like this, unless you know all the caveats and you know what you are doing.
# @app.post("/user/")
# async def create_user(user: UserIn) -> UserIn:
#     return user

# ---filter out the password field from the response model---

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None

# # Add an output model: We can instead create an input model with the plaintext password and an output model without it:

# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn) -> Any:
#     return user

# --- annotate the functin with one type but return more data ---

# class BaseUser(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None


# class UserIn(BaseUser):
#     password: str


# @app.post("/user/")
# async def create_user(user: UserIn) -> BaseUser:
#     return user

# --- Reurn a Respone Directly ---

# @app.get("/portal")
# async def get_portal(teleport: bool = False) -> Response:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return JSONResponse(content={"message": "Here's your interdimensional portal."})

# @app.get("/teleport")
# async def get_teleport() -> RedirectResponse:
#     return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# --- Return a Union, this will FAIL ---
# @app.get("/portal")
# async def get_portal(teleport: bool = False) -> Response | dict:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return {"message": "Here's your interdimensional portal."}

# --- Return a Union, this will WORK ---

# @app.get("/portal", response_model=None)
# async def get_portal(teleport: bool = False) -> Response | dict:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return {"message": "Here's your interdimensional portal."}

# --- Response Model encoding parameters ---

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float = 10.5
#     tags: list[str] = []


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }


# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
# async def read_item(item_id: str):
#     return items[item_id]

# --- Return sets ---

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float = 10.5


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
#     "baz": {
#         "name": "Baz",
#         "description": "There goes my baz",
#         "price": 50.2,
#         "tax": 10.5,
#     },
# }


# @app.get(
#     "/items/{item_id}/name",
#     response_model=Item,
#     response_model_include={"name", "description"},
# )
# async def read_item_name(item_id: str):
#     return items[item_id]


# @app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
# async def read_item_public_data(item_id: str):
#     return items[item_id]

# --- Return a list ---

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include=["name", "description"],
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude=["tax"])
async def read_item_public_data(item_id: str):
    return items[item_id]

# Use the path operation decorator's parameter response_model to define response models and especially to ensure private data is filtered out. Use response_model_exclude_unset to return only the values explicitly set.
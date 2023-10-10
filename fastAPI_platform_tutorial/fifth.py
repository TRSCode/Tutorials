from typing import Annotated, Union, List
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Body - Fields and Nested Models"}

# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title="The description of the item", max_length=300
#     )
#     price: float = Field(gt=0, description="The price must be greater than zero")
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     results = {"item_id": item_id, "item": item}
#     return results

# --- Nested Models with Pydantic ---

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list = []


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# --- declare a list of items with python type list (but now a string) ---

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     # tags: List[str] = [] (prior to Python 3.9)
#     # tags: list[str] = []
#     # Python has a special data type for sets of unique items: set
#     tags: set[str] = set()


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# --- submodel or nested model ---

# class Image(BaseModel):
#     # url: str
#     # special type for URLs: HttpUrl
#     url: HttpUrl
#     name: str


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     # image: Image | None = None
#     # attributes with lists of submodels
#     images: list[Image] | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# --- deeply nested models ---

# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     images: list[Image] | None = None


# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items: list[Item]


# @app.post("/offers/")
# async def create_offer(offer: Offer):
#     return offer

# --- Bodies of pure lists ---

# from fastapi import FastAPI
# from pydantic import BaseModel, HttpUrl

# app = FastAPI()


# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# @app.post("/images/multiple/")
# async def create_multiple_images(images: list[Image]):
#     # for image in images:
#     #     image.url
#     return images

# --- Bodies of arbitrary dicts ---

from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
from typing import Annotated, Union, List
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Declare Request Example Data"}

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

#     model_config = {
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 }
#             ]
#         }
#     }

# --- now a quicker way using Field and examples providing a similar JSON return ---

# class Item(BaseModel):
#     name: str = Field(examples=["Foo"])
#     description: str | None = Field(default=None, examples=["A very nice Item"])
#     price: float = Field(examples=[35.4])
#     tax: float | None = Field(default=None, examples=[3.2])


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int,
#     item: Annotated[
#         Item,
#         Body(
#             examples=[
#                 {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 }
#             ],
#         ),
#     ],
# ):
#     results = {"item_id": item_id, "item": item}
#     return results

# --- this example shows how to use multiple examples, but is not supported by Swagger UI ---
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Annotated[
#         Item,
#         Body(
#             examples=[
#                 {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 },
#                 {
#                     "name": "Bar",
#                     "price": "35.4",
#                 },
#                 {
#                     "name": "Baz",
#                     "price": "thirty five point four",
#                 },
#             ],
#         ),
#     ],
# ):
#     results = {"item_id": item_id, "item": item}
#     return results

# --- this example shows how to use multiple examples, but is supported by Swagger UI (see dropdown in Swagger UI) ---

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Annotated[
#         Item,
#         Body(
#             openapi_examples={
#                 "normal": {
#                     "summary": "A normal example",
#                     "description": "A **normal** item works correctly.",
#                     "value": {
#                         "name": "Foo",
#                         "description": "A very nice Item",
#                         "price": 35.4,
#                         "tax": 3.2,
#                     },
#                 },
#                 "converted": {
#                     "summary": "An example with converted data",
#                     "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
#                     "value": {
#                         "name": "Bar",
#                         "price": "35.4",
#                     },
#                 },
#                 "invalid": {
#                     "summary": "Invalid data is rejected with an error",
#                     "value": {
#                         "name": "Baz",
#                         "price": "thirty five point four",
#                     },
#                 },
#             },
#         ),
#     ],
# ):
#     results = {"item_id": item_id, "item": item}
#     return results

# --- extra data types ---


# Other data types¶
# Here are some of the additional data types you can use:

# *UUID:
# A standard "Universally Unique Identifier", common as an ID in many databases and systems.
# In requests and responses will be represented as a str.
# *datetime.datetime:
# A Python datetime.datetime.
# In requests and responses will be represented as a str in ISO 8601 format, like: 2008-09-15T15:53:00+05:00.
# *datetime.date:
# Python datetime.date.
# In requests and responses will be represented as a str in ISO 8601 format, like: 2008-09-15.
# *datetime.time:
# A Python datetime.time.
# In requests and responses will be represented as a str in ISO 8601 format, like: 14:23:55.003.
# *datetime.timedelta:
# A Python datetime.timedelta.
# In requests and responses will be represented as a float of total seconds.
# Pydantic also allows representing it as a "ISO 8601 time diff encoding", see the docs for more info.
# *frozenset:
# In requests and responses, treated the same as a set:
# In requests, a list will be read, eliminating duplicates and converting it to a set.
# In responses, the set will be converted to a list.
# The generated schema will specify that the set values are unique (using JSON Schema's uniqueItems).
# *bytes:
# Standard Python bytes.
# In requests and responses will be treated as str.
# The generated schema will specify that it's a str with binary "format".
# *Decimal:
# Standard Python Decimal.
# In requests and responses, handled the same as a float.
# You can check all the valid pydantic data types here: Pydantic data types.


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime | None, Body()] = None,
    end_datetime: Annotated[datetime | None, Body()] = None,
    repeat_at: Annotated[time | None, Body()] = None,
    process_after: Annotated[timedelta | None, Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
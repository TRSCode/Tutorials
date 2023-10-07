from typing import Annotated, Union
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Path Parameters and Numeric Validations"}

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q: Annotated[str | None, Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/{item_id}")
# async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/{item_id}")
# async def read_items(
#     q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/{item_id}")
# async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")], q: str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# --- greater than or equal to, less than or equal to, and use with float

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
#     q: str,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

# ----------------- Part 2 ----------------- 
# Query Parameters and String Validations

@app.get("/")
async def root():
    return {"message": "Hello World Part 2"}


# @app.get("/items/")
# async def read_items(q: str | None = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# additional validation

@app.get("/items/")
async def read_items(
    # q: Annotated[str | None, Query(max_length=50)] = None
    # q: Annotated[str | None, Query(min_length=3, max_length=50)] = None
    # pattern validation replaced regex validation
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None
    ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

from typing import Annotated, Union
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

# @app.get("/items/")
# async def read_items(
#     # q: Annotated[str | None, Query(max_length=50)] = None
#     # q: Annotated[str | None, Query(min_length=3, max_length=50)] = None
#     # --- pattern validation replaced regex validation
#     # q: Annotated[
#     #     str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
#     # ] = None
#     # --- now make it required
#     # q: Annotated[str, Query(min_length=3)]
#     # --- now make it required and give it a default value (literal value ... Ellipsis )
#     # q: Annotated[str, Query(min_length=3)] = ...
#     # --- now make it default to None and required with Ellipsis
#     q: Annotated[str | None, Query(min_length=3)] = ...
#     ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# --- query parameter list / multiple values
# @app.get("/items/")
# async def read_items(
#     q: Annotated[Union[list[str], None], Query()] = None
#     # q: Annotated[list[str] | None, Query()] = None
#     ):
#     query_items = {"q": q}
#     return query_items
# http://localhost:8000/items/?q=foo&q=bar
# you can use q multiple times as above

# --- query parameter list / multiple values with defaults
# @app.get("/items/")
# async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
#     query_items = {"q": q}
#     return query_items
# # http://localhost:8000/items/

# --- using list
# @app.get("/items/")
# async def read_items(q: Annotated[list, Query()] = []):
#     query_items = {"q": q}
#     return query_items
# http://localhost:8000/items/?q=foo&q=bar&q=string

# --- declare more metadata

# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None,
#         Query(
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#         ),
#     ] = None
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# --- alias query parameter

# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
# this allows for this http://127.0.0.1:8000/items/?item-query=foobaritems

# --- deprecated query parameter - allows you to leave in the parameter but will let the client know it is deprecated

# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None,
#         Query(
#             alias="item-query",
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#             max_length=50,
#             pattern="^fixedquery$",
#             deprecated=True,
#         ),
#     ] = None
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# --- exclude a query parameter from the schema - this will not show up in the docs
@app.get("/items/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
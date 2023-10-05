from fastapi import FastAPI

app = FastAPI()

# ----------------- Part 2 ----------------- 
# Query Parameters and String Validations

@app.get("/")
async def root():
    return {"message": "Hello World Part 2"}


@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

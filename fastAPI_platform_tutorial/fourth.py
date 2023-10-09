from typing import Annotated, Union
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Body - Multiple Parameters"}
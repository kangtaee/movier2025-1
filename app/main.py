from fastapi import FastAPI
import pandas as pd
import uvicorn
from resolver import random_items, random_genres_items, random_genres_items_best# random_genres_items_best_fantasy
from starlette.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello MovieR"}

@app.get("/all")
async def all_movies():
    result = random_items()
    return {"result": result}

@app.get("/genres/{genre}")
async def genre_movies(genre: str):
    result = random_genres_items(genre)
    return {"result": result}

@app.get("/genres/{genre}")
async def genre_movies_best(genre: str):
    result = random_genres_items_best(genre)
    return {"result": result}

@app.get("/genresbest/{genre}")
async def genre_best_movies_best(genre: str):
    result = random_genres_items_best(genre)
    return {"result": result}

@app.get("/item_based/{genre}")
async def item_based(genre: str):
    result = random_genres_items_best(genre)
    return {"result": result}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
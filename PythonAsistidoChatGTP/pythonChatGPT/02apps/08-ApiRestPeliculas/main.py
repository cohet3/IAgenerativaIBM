from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Modelo de datos para una película
class Movie(BaseModel):
    title: str
    year: int
    description: str
    director: str


# Base de datos en memoria (simulación)
movies_db = [
    {"title": "Inception", "year": 2010,
     "description": "A thief who steals corporate secrets through the use of dream-sharing technology.",
     "director": "Christopher Nolan"},
    {"title": "The Matrix", "year": 1999,
     "description": "A computer hacker learns about the true nature of reality and his role in the war against its controllers.",
     "director": "The Wachowskis"},
    {"title": "Interstellar", "year": 2014,
     "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
     "director": "Christopher Nolan"}
]


# Endpoint para obtener la lista de todas las películas
@app.get("/movies/", response_model=List[Movie])
def get_movies():
    return movies_db


# Endpoint para obtener una película por título
@app.get("/movies/{title}", response_model=Movie)
def get_movie(title: str):
    for movie in movies_db:
        if movie["title"].lower() == title.lower():
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


# Endpoint para agregar una nueva película
@app.post("/movies/", response_model=Movie)
def add_movie(movie: Movie):
    for m in movies_db:
        if m["title"].lower() == movie.title.lower():
            raise HTTPException(status_code=400, detail="Movie already exists")
    movies_db.append(movie.dict())
    return movie


# Endpoint para actualizar una película existente
@app.put("/movies/{title}", response_model=Movie)
def update_movie(title: str, movie: Movie):
    for i, m in enumerate(movies_db):
        if m["title"].lower() == title.lower():
            movies_db[i] = movie.dict()
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


# Endpoint para eliminar una película
@app.delete("/movies/{title}", response_model=Movie)
def delete_movie(title: str):
    for i, m in enumerate(movies_db):
        if m["title"].lower() == title.lower():
            deleted_movie = movies_db.pop(i)
            return deleted_movie
    raise HTTPException(status_code=404, detail="Movie not found")


# Si se ejecuta el script directamente, se inicia el servidor de desarrollo
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

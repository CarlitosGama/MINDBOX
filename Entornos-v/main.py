from fastapi import FastAPI, HTTPException, status
from database import create_db_and_tables, SessionDep
from user import UserModel
from random import randint
from sqlmodel import select
from schemas import movieSchema
from models import MoviesModel

app = FastAPI()

"""
GET-OBTENER ALGO
POST-CREAR ALGO
PUT-ACTUALIZAR ALGO
DELETE-ELIMINAR ALGO
"""

create_db_and_tables()

#estos metodos son para la api anterior 
"""
@app.post("/users")
async def root(user_data: UserSchema, database: SessionDep):
    user = UserModel(
        name=user_data.name,
        last_name=user_data.last_name,
        email=user_data.email,
        phone=user_data.phone
    )

    database.add(user)
    database.commit()
    database.refresh(user)

    return user

@app.get("/users")
async def get_users(database: SessionDep):
    statement = select(UserModel)
    results = database.exec(statement)
    items = results.all()
    return items

@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int, database: SessionDep):
    user = database.get(UserModel, user_id)

    if not user:
     raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    return user
"""
@app.post("/movies")
async def rootm(movie_data: movieSchema, database: SessionDep):
    movie = MoviesModel(
        name= movie_data.name,
        year_peli=movie_data.year_peli ,
        long=movie_data.long,
        director=movie_data.director,
        classification=movie_data.classification,
        gender=movie_data.gender
    )

    database.add(movie)
    database.commit()
    database.refresh(movie)

    return movie 

@app.get("/movie")
async def get_movie(database: SessionDep):
    statement = select(MoviesModel)
    results = database.exec(statement)
    items = results.all()
    return items

@app.get("/movie/{movie_id}")
async def get_movies_by_id(movie_id: int, database: SessionDep):
    movie = database.get(MoviesModel, movie_id)

    if not movie:
     raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    return movie
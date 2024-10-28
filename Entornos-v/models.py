from sqlmodel import  SQLModel,Field
from datetime import datetime

class MoviesModel(SQLModel, table=True):
    __tablename__= "movies"

    id: int = Field(primary_key=True)
    name: str
    year_peli: int
    long: int 
    director: str
    classification: str
    gender: str

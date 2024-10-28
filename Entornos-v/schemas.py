from pydantic import BaseModel
from datetime import datetime

class movieSchema(BaseModel):
    name: str
    year_peli: int
    long: int 
    director: str
    classification: str
    gender: str
   
   
   
    """
    name: str
    last_name: str
    email: str
    phone: str
    """
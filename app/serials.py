from pydantic import BaseModel
from datetime import date

class Serial(BaseModel):
    title: str
    studio: str
    duration: int
    date: date
    summary: str
    genres: str = None

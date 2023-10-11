from fastapi import FastAPI, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

app.title = 'Users and Directions'
app.version = '1.0'


class User(BaseModel):
    id: Optional[int] = None
    first_name: str = Field()
    last_name: str
    email: str
    password: str
    addresses: List[str] = []

class Direction(BaseModel):
    id: int
    address_1: str
    address_2: str
    city:str
    state:str
    zip: int
    country: str

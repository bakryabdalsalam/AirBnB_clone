#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel

class Review(BaseModel):
    place_id: str = ""
    user_id: str = ""
    text: str = ""

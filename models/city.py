#!/usr/bin/python3
"""It is a city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This represents a city
    Attributes:
        state_id (str): The state id
        name (str): Name of the city
    """

    state_id = ""
    name = ""

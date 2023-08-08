#!/usr/bin/python3
"""This defines state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """It represents a state
    Attributes:
        name (str): A name of the state
    """

    name = ""

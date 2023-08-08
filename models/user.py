#!/usr/bin/python3
"""This defines the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Represents a user
    Attributes:
        email (str): Email of the user
        password (str): Password of the user
        first_name (str): The users first name
        last_name (str): last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

#!/usr/bin/python3
"""It defines a review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This represents a review
    Attributes:
        place_id (str): the place id
        user_id (str): user id
        text (str): text of the review
    """

    place_id = ""
    user_id = ""
    text = ""

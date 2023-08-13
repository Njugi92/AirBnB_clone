#!/usr/bin/python3
"""This defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Representation of the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """It initializes a new BaseModel.
        Artributes:
            *args (any): Unused.
            **kwargs (dict): The key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """It updates updated_at with current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """This returns dictionary of the BaseModel instance.
        Also includes the key/value pairs __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """It returns print or str representations of BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

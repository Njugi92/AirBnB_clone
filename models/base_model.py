#!/usr/bin/python3
"""This defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Representation of the BaseModel of the HBnB project."""
    objects = []

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

    @classmethod
    def all(self):
        """The function to print all object from specific class"""
        print((str(model) for model in self.objects))

    @classmethod
    def count(self):
        """To print the len of object in specific class"""
        print(len(self.objects))

    @classmethod
    def show(self, id):
        """Function to show the object in specific class using id"""
        for object in self.objects:
            if object.id == id:
                print(object)
                return
            print("** no instance found **")

    @classmethod
    def update(self, id, attribute_name, attribute_value):
        """Function to update object attributes"""
        for value in storage.all().values():
            if value.id == id:
                value.__dict__[attribute_name] = attribute_value
                storage.save()
        for object in self.objects:
            if object.id == id:
                object.__dict__[attribute_name] = attribute_value
                return
            print("** no instance found **")

    @classmethod
    def update_dict(self, id, attribute_dict):
        """Function to update the object attributes from dict"""
        for k, v in attribute_dict.items():
            self.update(id, k, v)

    @classmethod
    def destroy(self, id):
        """The function to remove object from class using its id"""
        k = self.__name__ + '.' + id
        if k in storage.all():
            for i in range(len(self.objects)):
                if self.objects[i].id == id:
                    self.objects.pop(i)
            storage.all().pop(k)
            storage.save()
            return
        print("** no instance found **")

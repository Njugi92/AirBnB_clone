#!/usr/bin/python3
"""
base_model module :
this module contain BaseModel class this class consider
our base calss for our AirBnB project.
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """Base Model Class:
    this class has a lot of functions and consider the base class of
    many others classe.
    """
    objects = []

    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

        self.__class__.objects.append(self)

    def __str__(self):
        """print object representation"""

        return ('[' + type(self).__name__ + '] (' +
                str(self.id) + ') ' + str(self.__dict__))

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    @classmethod
    def all(self):
        """function to print all object from specific class"""
        print([str(model) for model in self.objects])

    @classmethod
    def count(self):
        """to print the len of object in specific class"""
        print(len(self.objects))

    @classmethod
    def show(self, id):
        """to show the object in specific class using id"""
        for object in self.objects:
            if object.id == id:
                print(object)
                return
        print("** no instance found **")

    @classmethod
    def update(self, id, attribute_name, attribute_value):
        """to update the object attributes """

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
        """to update the object attributes from dict"""
        for key, value in attribute_dict.items():
            self.update(id, key, value)

    @classmethod
    def destroy(self, id):
        """to remove object from class using its id"""
        key = self.__name__ + '.' + id
        if key in storage.all():
            for i in range(len(self.objects)):
                if self.objects[i].id == id:
                    self.objects.pop(i)
            storage.all().pop(key)
            storage.save()
            return
        print("** no instance found **")

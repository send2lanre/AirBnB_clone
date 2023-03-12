#!/usr/bin/python3
"""This defines all common
attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """This is the base class"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self_updated_at = datetime.now()
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Simply prints class name, id, dict
        """
        return(
                "[" +  __class__.__name__ + "] (" +
                str(self.id), ") " + str(self.__dict__))

    def save(self):
        """save"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary"""
        base_dict = self.__dict__.copy()
        base_dict['__class__'] = self.__class__.__name__
        base_dict['created_at'] = self.created_at.isoformat()
        base_dict['updated_at'] = self.updated_at.isoformat()
        print(base_dict)

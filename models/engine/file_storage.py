#!/usr/bin/python3
"""serialize to json, deserialize to instance"""
import json
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

class FileStorage:
    """Serialization and deserialization"""
    __file.path = 'file.json'
    __objects = {}
    def all(self):
        """return dictionary objects"""
        return FileStorage.__objects
    def new(self, obj):
        """sets in __objects the object
        with key <obj classname>.id
        """
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj
    def save(self):
        """Serializes python file"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as json_file:
            new_dict = {key: obj.to_dict() for key, obj in
                    FileStorage.__objects.items()}
            json.dump(new_dict, json_file)
    def reload(self):
        """deserializes json file"""
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as json_file:
                deSerial = json.load(json_file)
                for key, val in deSerial.items():
                    FileStorage.__objects[key] = eval(
                            val['__class__'])(**val)

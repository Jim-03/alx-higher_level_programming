#!/usr/bin/python3
"""defines a base class"""
import json


class Base:
    """The base class."""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializes the base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string representation."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string representation to a file."""
        if list_objs is None:
            list_objs = []

        with open(cls.__name__ + ".json", 'w') as file:
            data = []
            for obj in list_objs:
                data.append(obj.to_dictionary())
            file.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """returns a list of json string representation."""
        if json_string is None or len(json_string) == 0:
                return '[]'
        new = json.loads(json_string)
        return new

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances."""
        fname = cls.__name__ + '.json'
        try:
            with open(fname, 'r') as file:
                data = file.read()
                dict_instances = cls.from_json_string(data)
                list_instances = []
                for obj in dict_instances:
                    list_instances.append(cls.create(**obj))
                return list_instances
        except FileNotFoundError:
            return []

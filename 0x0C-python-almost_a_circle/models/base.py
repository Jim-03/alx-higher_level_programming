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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in csv."""
        with open(cls.__name__ + '.csv', 'w', newline = '') as file:
            fsave = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    fsave.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    fsave.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes the csv."""
        try:
            with open(cls.__name__ + '.csv', 'r', newline='') as file:
                fload = csv.reader(file)
                list_instances = []
                for row in fload:
                    if cls.__name__ == "Rectangle" and len(row) == 5:
                        dict_data = {'id': int(row[0]), 'width': int(row[1]), 'height': int(row[2]),
                                     'x': int(row[3]), 'y': int(row[4])}
                        list_instances.append(cls.create(**dict_data))
                    elif cls.__name__ == "Square" and len(row) == 4:
                        dict_data = {'id': int(row[0]), 'size': int(row[1]), 'x': int(row[2]),\
                                'y': int(row[3])}
                        list_instances.append(cls.create(**dict_data))
                return list_instances
        except FileNotFoundError:
            return []

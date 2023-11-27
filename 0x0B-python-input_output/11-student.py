#!/usr/bin/python3
"""Module contans the class Student based on 10-student.py
"""


class Student:
    """Defines the properties of a student.

        Attributes:
            first_name (str): First name
            last_name (str): last name
            age (int): age

    """

    def __init__(self, first_name, last_name, age):
        """Creates new instances of a student.

        Args:
            first_name (str): first name of student.
            last_name (int): last name of student.
            age (int): age of student.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance

        if attrs is a list of strings, only attr names contained in
        this list must be retrieved.
        Otherwise, all attributes must be retrieved.

        Returns:
            dict: dictionary representation.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass

        return new_dict

    def reload_from_json(self, json):
        """Replaces all attriutes of the Student instance.

        Args:
            json (dict): json object.
        """
        # print("Type json --> {}".format(type(jon)))
        self.__dict__.update(json)

#!/usr/bin/python3
"""
Class Student
"""


class Student():
    """
    Constructor
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            new_vars = {}
            for att in attrs:
                if hasattr(self, att):
                    # Conseguimos su valor y lo agregamos al dicc
                    new_vars[att] = getattr(self, att)
            return new_vars
        return vars(self)

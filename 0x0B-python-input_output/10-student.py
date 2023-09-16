#!/usr/bin/python3

"""This module defines a basic structure for Student class
Than can be used to create new Student objects with:
public instance attrs like: first_name, last_name and age

"""


class Student:
    """Definiation of the Student class
    Args:
        first_name (str):
            first name of the Student
        last_name (str):
            last/family name of the student
        age (int):
            age of the student

    """
    def __init__(self, first_name, last_name, age):
        """magic method call at instanciation of the student class
        to set the first_name the last_name and the age of a new
        student

        Args:
            first_name (str):
                first name of the Student
            last_name (str):
                last/family name of the student
            age (int):
                age of the student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json: returns the dict representation of a Student object

        Args:
            attrs (list):
                list of string representing the attributes to retreive

        Returns:
            (dict): the dict representation of the object

        """
        if type(attrs) is not list:
            return self.__dict__

        dict_rep: dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                dict_rep.update({attr: self.__dict__[attr]})

        return dict_rep

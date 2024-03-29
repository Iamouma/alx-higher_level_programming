#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """This represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.
        Args:
            first_name (str): Is the first name of the Student.
            last_name (str): Is the last name of the Student.
            age (int): Is the age of the Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This gets a dictionary representation of the Student,"""
        return self.__dict__

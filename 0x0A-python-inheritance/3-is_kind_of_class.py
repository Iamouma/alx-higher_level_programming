#!/usr/bin/python3
"""Defines a class and an inheritated class checking function."""


def is_kind_of_class(obj, a_class):
    """
    This function checks if an object is an instance or inheritated instance of a class.
    
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        If the obj is an instance or inheritated instance of a class - True.
        Otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False

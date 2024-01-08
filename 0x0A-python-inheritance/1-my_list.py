#!/usr/bin/python3
"""Defines a subclass list class MyList."""


class MyList(list):
    """A subclass of the built-in list class."""
    def print_sorted(self):
        """Prints a sorted list in an ascending order."""
        print(sorted(self))

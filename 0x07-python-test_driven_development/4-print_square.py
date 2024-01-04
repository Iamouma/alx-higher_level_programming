#!/usr/bin/python3
"""
This function defines a function for printing a square using the # character.
"""


def print_square(size):
    """
    Print a square with the # character.

    Args:
        size (int): The height and width of the square.

    Raises:
        TypeError: If the size is not an integer.
        ValueError: If size is < 0
    """


    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

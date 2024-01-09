#!/usr/bin/python3
"""Defines a file writing function."""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF8 text file.
    Args:
        filename (str): Is the name of the file to write.
        text (str): Is the text to write the file.
    Returns:
        This requires the number of characters written.
    """
    with open(filename, "w", encoding="utf8") as f:
        return f.write(text)

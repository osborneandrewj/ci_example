"""This is a project for CS 362 exploring continuous integration

Authors: Andrew Osborne, John Oliver, nextAuth
Date: Spring Quarter 2023
"""


def conv_num(num_str):
    """Converts a string into a base 10 number

    Takes a string (num_str) and converts it into a base
    10 number (conv_number), and returns that number.

    Returns:
    conv_num as an int
    """

    if isinstance(num_str, str) is not True:
        return None

    if len(num_str) == 0:
        return None

    conv_number = 0

    return conv_number


def my_datetime(num_sec):
    """
    Takes an integer as an input that represents a number of seconds since
    01/01/1970, converts it to a date and returns it as a string

    Returns:
    new_datetime as a string
    """

    if isinstance(num_sec, int) is not True:
        return None

    new_datetime = ''

    return new_datetime


def conv_endian(num, endian='big'):
    """Docstring here

    Returns:
    """

    return None

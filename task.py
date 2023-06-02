"""This is a project for CS 362 exploring continuous integration

Authors: Andrew Osborne, nextAuth, nextAuth
Date: Spring Quarter 2023
"""

import string

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

    if num_str.count('.') > 1:
        return None

    for i in num_str:
        if i != '.':
            if string.hexdigits.find(i) is False:
                return None

    conv_number = 0

    return conv_number


def my_datetime(num_sec):
    """Docstring here

    Returns:
    """

    return None


def conv_endian(num, endian='big'):
    """Docstring here

    Returns:
    """

    return None

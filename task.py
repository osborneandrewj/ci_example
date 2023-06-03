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

    for c in num_str:
        if c not in (".", "-"):
            if string.hexdigits.find(c) == -1:
                return None

    conv_number = 0
    negative_flag = False
    float_flag = False
    decimal_place = 0

    for i, c in enumerate(num_str):
        if i == 0:
            if c == "-":
                negative_flag = True
                continue
        if c == ".":
            float_flag = True
            decimal_place = i+1
            continue
        # get place value
        if float_flag is True:
            p_value = 10**(-i - decimal_place)
        else:
            p_value = 10**(len(num_str) - (i+1))
        num_value = ord(c) - 48
        conv_number += p_value*num_value

    if negative_flag is True:
        conv_number = conv_number * -1
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

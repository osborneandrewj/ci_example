"""This is a project for CS 362 exploring continuous integration

Authors: Andrew Osborne, John Oliver, nextAuth
Date: Spring Quarter 2023
"""

import string


def is_str_valid(num_str):
    """Searches a string for invalid characters

    Returns:
    False if invalid characters are found, True if none are found
    """

    if isinstance(num_str, str) is not True:
        return False

    if len(num_str) == 0:
        return False

    if num_str.count('.') > 1:
        return False

    if num_str[0] == "0" and num_str[1] == "x":
        for i in range(2, len(num_str) - 1):
            if string.hexdigits.find(num_str[i]) == -1:
                return False
    else:
        for c in num_str:
            if c not in (".", "-"):
                if string.hexdigits.find(c) == -1:
                    return False

    return True


def convert_hex(num_str):
    """Converts a hexidecimal string into number

    Returns:
    the hexidecimal input as a number"""

    hex_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14,
                "F": 15}
    hex_num = 0
    hex_str = num_str[2:len(num_str)]

    for i, c in enumerate(hex_str):
        # get place value
        p_value = (16**(len(hex_str) - (i+1)))
        if c in hex_dict:
            num_value = hex_dict[c]
        else:
            num_value = ord(c) - 48
        hex_num += p_value*num_value

    return hex_num


def conv_num(num_str):
    """Converts a string into a base 10 number

    Takes a string (num_str) and converts it into a base
    10 number (conv_number), and returns that number.

    Returns:
    conv_num as an int
    """

    if is_str_valid(num_str) is False:
        return None

    conv_number = 0

    if num_str[0] == "0" and num_str[1] == "x":
        conv_number = convert_hex(num_str)
        return conv_number

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
            decimal_place = i
            continue
        # get place value
        if float_flag is True:
            p_value = 10**(-(i - decimal_place))
        else:
            p_value = 10**(len(num_str) - (i+1))
        num_value = ord(c) - 48
        conv_number += p_value*num_value

    if negative_flag is True:
        conv_number = conv_number * -1
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
    num_days = num_sec // 86400

    common_year = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    leap_year = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    current_year = 1970
    current_month = 1
    current_day = 1

    while num_days > 0:

        if is_leap_year(current_year) is True:
            if num_days >= 366:
                num_days = num_days - 366
                current_year = current_year + 1
            else:
                if num_days > 0:
                    for i in range(1, (len(leap_year) + 1)):
                        if (num_days - leap_year[i]) < 0:
                            current_month = i
                            break
                        else:
                            num_days = num_days - leap_year[i]
                            current_month = i
                    current_day = current_day + num_days
                    num_days = 0      
        else:
            if num_days >= 365:
                num_days = num_days - 365
                current_year = current_year + 1
            else:
                if num_days > 0:
                    for i in range(1, (len(common_year) + 1)):
                        if (num_days - common_year[i]) < 0:
                            current_month = i
                            break
                        else:
                            num_days = num_days - common_year[i]
                            current_month = i
                    current_day = current_day + num_days
                    num_days = 0

    if current_month < 10:
        month_str = "0" + str(current_month)
    else:
        month_str = str(current_month)

    if current_day < 10:
        day_str = "0" + str(current_day)
    else:
        day_str = str(current_day)

    new_datetime = month_str + "-" + day_str + "-" + str(current_year)
    return new_datetime


def is_leap_year(year):
    """
    Takes an int representing a year and determines whether or not that
    year is a leap_year

    Returns:
    A boolean
    """

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def conv_endian(num, endian='big'):
    """Docstring here

    Returns:
    """

    return None

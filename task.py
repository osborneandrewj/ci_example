"""This is a project for CS 362 exploring continuous integration

Authors: Andrew Osborne, John Oliver, Jonathan Alexander
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
                    month_and_days = get_current_month(leap_year, num_days)
                    current_month = month_and_days[0]
                    current_day = current_day + month_and_days[1]
                    num_days = 0
        else:
            if num_days >= 365:
                num_days = num_days - 365
                current_year = current_year + 1
            else:
                if num_days > 0:
                    month_and_days = get_current_month(common_year, num_days)
                    current_month = month_and_days[0]
                    current_day = current_day + month_and_days[1]
                    num_days = 0

    new_datetime = build_string(current_year, current_month, current_day)
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


def build_string(year, month, day):
    """
    Takes three ints representing a given year, a given month, and a
    given day and builds a string representation of the date

    Returns:
    A string
    """

    if month < 10:
        month_str = "0" + str(month)
    else:
        month_str = str(month)

    if day < 10:
        day_str = "0" + str(day)
    else:
        day_str = str(day)

    return month_str + "-" + day_str + "-" + str(year)


def get_current_month(calendar, days):
    """
    Calculates the month and the number of remaining days

    Returns:
    A tuple representing the month and number of remaining days, both
    as an int
    """

    for i in range(1, (len(calendar) + 1)):
        if (days - calendar[i]) < 0:
            current_month = i
            break
        else:
            days = days - calendar[i]
            current_month = i

    return current_month, days


def conv_endian(num, endian='big'):
    """Converts an integer into a hexadecimal number

    Takes an integer (num) and converts into a hexadecimal number (hex_num)
    and return that number

    Returns:
    hex_num as a string
    """
    hex_symbols = '0123456789ABCDEF'
    hex_num = ''
    
    while num > 0:
        hex_symbol = hex_symbols[num & 0xF]
        hex_num = hex_symbol + hex_num
        num >>= 4

    hex_num = hex_num.zfill(len(hex_num) + (len(hex_num) % 2))
    hex_num = ' '.join(hex_num[i:i + 2] for i in range(0, len(hex_num), 2))
    
    return hex_num

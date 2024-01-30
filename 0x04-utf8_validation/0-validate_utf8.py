#!/usr/bin/python3
"""
Tasks

0. UTF-8 Validation

Write a method that determines if a given data set represents a valid UTF-8
encoding.

    - Prototype: def validUTF8(data)
    - Return: True if data is a valid UTF-8 encoding, else return False
    - A character in UTF-8 can be 1 to 4 bytes long
    - The data set can contain multiple characters
    - The data will be represented by a list of integers
    - Each integer represents 1 byte of data, therefore you only need to handle
    the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    Validates the data as a UTF-8 Character
    """
    bytes_num = 0

    for byte in data:
        if bytes_num == 0:
            if (byte & 0x80) == 0x00:
                bytes_num = 0
            elif (byte & 0xE0) == 0xC0:
                bytes_num = 1
            elif (byte & 0xF0) == 0xE0:
                bytes_num = 2
            elif (byte & 0xF8) == 0xF0:
                bytes_num = 3
        else:
            if (byte & 0xC0) == 0x80:
                bytes_num -= 1
            else:
                return False
    return bytes_num == 0

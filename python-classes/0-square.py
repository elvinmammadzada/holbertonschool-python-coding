#!/usr/bin/python3
"""
This module defines a class Square with a private size attribute.
No validation is done on size.
"""


class Square:
    """Square with private size, no validation."""

    def __init__(self, size):
        self.__size = size

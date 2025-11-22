#!/usr/bin/python3
"""This module defines a class Square with a private size attribute, no validation."""

class Square:
    """Square with private size, no validation."""
    def __init__(self, size):
        self.__size = size

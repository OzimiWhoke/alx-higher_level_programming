#!/usr/bin/python3
"""
contains a function that appends a string
"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""
contains the read_file function
"""


def read_file(filename=""):

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

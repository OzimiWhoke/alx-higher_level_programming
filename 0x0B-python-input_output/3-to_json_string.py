#!/usr/bin/python3
"""
JSON string
"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    returns json.dumps(my_obj)

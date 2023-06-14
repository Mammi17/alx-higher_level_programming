#!/usr/bin/python3
"""that contains the "save_to_json_file" function"""

import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation"""
    with open(filename, 'w+') as f:
        json.dump(my_obj, f)

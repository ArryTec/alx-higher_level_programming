#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file"""

import json
import sys

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

    my_list += sys.argv[1:]

    save_to_json_file(my_list, "add_item.json")


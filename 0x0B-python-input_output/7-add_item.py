#!/usr/bin/python3

"""this is a script that adds all arguments to a Python list,
and then save them to a file
"""

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    import sys

    try:
        py_list: list = load_from_json_file("add_item.json")
    except Exception:
        py_list = []

    for idx in range(1, len(sys.argv)):
        py_list.append(sys.argv[idx])

    save_to_json_file(py_list, "add_item.json")

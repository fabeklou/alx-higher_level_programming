#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    name_list = dir(hidden_4)
    for name in name_list:
        if not name.startswith("__"):
            print("{:s}".format(name))

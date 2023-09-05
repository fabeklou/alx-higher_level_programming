#!/usr/bin/python3
def magic_string() -> str:
    magic_string.iter: int = getattr(magic_string, "iter", 0) + 1
    return (magic_string.iter * "BestSchool, ")[:-2]

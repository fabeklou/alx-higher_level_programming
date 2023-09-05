#!/usr/bin/python3
def magic_string() -> str:
    iter: int = globals()[list(globals())[-1]]
    return (iter * "BestSchool, ")[:-2]

#!/usr/bin/python3

"""Defines a function that prints a text with 2 new lines
after each of these characters `.`, `?` and `:`

"""


def text_indentation(text: str):
    """text_indentation print a text with 2 lines
    after each of these characters `.`, `?` and `:`

    Args:
        text (str): the string to be printed

    Returns: Nothing

    Raises:
        TypeError: if text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    f_chars: str = ".?:"
    to_avoid: str = ' '
    text_size: int = len(text)
    idx: int = 0
    """
        `f_chars`: is a string containing the characters that should precede
        the 2 new lines 
        `to_avoid`: is a space character  used to avoid printing unnecessary
        spaces
        `text_size`: is the length of the given string
        `idx`: is used to get a character in the string and is initialy set
        to 0 as strings are zero indexed

    """

    while idx < text_size:
        if text[idx] in f_chars:
            print("{:s}\n".format(text[idx]))
            idx += 1
            while text[idx] is to_avoid:
                idx += 1
            continue
        if text[idx] == " ":
            print(text[idx], end="")
            idx += 1
            while text[idx] is to_avoid:
                idx += 1
            continue
        print(text[idx], end="")
        idx += 1


if __name__ == "__main__":
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres""")

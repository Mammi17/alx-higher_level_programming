#!/usr/bin/python3
""" text of indentation"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after
    each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    string = ['.', '?', ':']

    # Removes the space after special chars
    ind = 0
    for it in text:
        if it in string:
            if text[ind + 1] == " ":
                text = text[:ind + 1] + text[ind + 2:]
        else:
            ind += 1
    ind = 0
    for it in text:
        if it in string:
            text = text[:ind + 1] + '\n\n' + text[ind + 1:]
            ind += 3
        else:
            ind += 1

    print(text, end="")

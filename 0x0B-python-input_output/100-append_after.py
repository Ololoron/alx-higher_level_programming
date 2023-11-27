#!/usr/bin/python3
"""Module contains the function appent_after
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
    After each line containing a specific string

    Attr:
        fileaname (str): name of file. Defaults to "".
        search_string(str,optional): string to search. Defaults to "".
        new_string (str, optional): string to append. Defaults to "".
    """
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string

        fo.write(s)

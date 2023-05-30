#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        b = fct(*args)
        return b
    except Exception as a:
        print("Exception: {}".format(a), file=sys.stderr)
        return None

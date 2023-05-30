#!/usr/bin/python3

def safe_print_integer(value):
     """Print an integer with "{:d}".format().
    Args:
        value (int): The integer
    Returns: False - True.
    """
    try:
        print("{:d}".format(value))
        return True
    except:
        return False

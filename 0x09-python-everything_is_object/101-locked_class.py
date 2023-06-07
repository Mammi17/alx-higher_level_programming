#!/usr/bin/python3
"""class LockedClass with no class or object attribute"""


class LockedClass:
    """prevents the user from dynamically creating new instance"""

    __slots__ = ["first_name"]

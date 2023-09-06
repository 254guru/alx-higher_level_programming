#!/usr/bin/python3
"""
locked class module
"""


class LockedClass(object):
    """
    a locked class module with no class object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first name.
    """
    __slots__ = 'first_name'

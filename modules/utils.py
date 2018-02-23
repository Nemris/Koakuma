"""Module for shared functions."""

__author__ = "Death Mask Salesman"

import sys as _sys

def deduplicate_list(list_with_dups):
    """
    Removes duplicate entries from a list.

    :param list_with_dups: list to be purged
    :type lost_with_dups:  list
    :returns:              a list without duplicates
    :rtype:                list
    """

    return list(set(list_with_dups))

def print_warn(msg):
    """
    Prints a warning message to stderr.

    :param msg: the warning message to be printed
    :type msg:  str
    """

    print("[ W ] {0}".format(msg), file = _sys.stderr)

def exit_fatal(msg):
    """
    Prints an error message to stderr and exits with code 1.

    :param msg: the error message to be printed
    :type msg:  str
    """

    print("[ F ] {0}".format(msg), file = _sys.stderr)

    exit(1)

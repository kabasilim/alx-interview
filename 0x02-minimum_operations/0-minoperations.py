#!/usr/bin/python3
"""This file contains the minOperations function"""


def minOperations(n):
    """This calculates the fewest number of
    operations needed to result in exactly n H
    characters in a file"""
    if (isinstance(n, int) and (n > 0)):
        operations = 0
        paste = 1
        latest_copy = 0

        while paste < n:
            if latest_copy == 0:
                latest_copy = paste
                paste += latest_copy
                operations += 2
                continue
            target = n - paste
            if target < latest_copy:
                return 0
            if target % paste == 0:
                latest_copy = paste
                paste += latest_copy
                operations += 2
            else:
                paste += latest_copy
                operations += 1
        if paste == n:
            return operations
        else:
            return 0
    return 0

#!/usr/bin/python3
"""This file contains the validUTF8 function"""


def validUTF8(data):
    """This function determines if a given data set
    represents a valid UTF-8 encoding
    """
    # Initialize a variable to keep track of the number of continuation bytes
    num_continuation_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        if num_continuation_bytes == 0:
            if byte >> 5 == 0b110 or byte >> 5 == 0b1110:
                num_continuation_bytes = 1
            elif byte >> 4 == 0b1110:
                num_continuation_bytes = 2
            elif byte >> 3 == 0b11110:
                num_continuation_bytes = 3
            elif byte >> 7 == 0b1:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_continuation_bytes -= 1
    return num_continuation_bytes == 0

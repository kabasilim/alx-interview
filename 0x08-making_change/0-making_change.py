#!/usr/bin/python3
"""This file contains the make_change function"""


def makeChange(coins, total):
    """The makeChange function"""

    if total <= 0:
        return 0
    sorted_coins = sorted(coins, reverse=True)

    present_value = 0
    change = 0
    coin_index = 0
    length = len(sorted_coins)

    while (present_value < total) and (coin_index < length):
        res = present_value + sorted_coins[coin_index]
        if res < total:
            change += 1
            present_value += sorted_coins[coin_index]
        elif res > total:
            coin_index += 1
        elif res == total:
            change += 1
            return change
        else:
            pass
    return -1

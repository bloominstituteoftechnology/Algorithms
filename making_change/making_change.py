#!/usr/bin/env python3

import sys


def making_change(amount, denominations=[1, 5, 10, 25, 50], cache=[]):
    arr = [0 for i in range(amount + 1)]
    arr[0] = 1
    for coin in denominations:
        for higherAmount in range(coin, amount + 1):
            offset = higherAmount - coin
            if offset >= 0:
                arr[higherAmount] += arr[offset]
    return arr[amount]

# 1:1 - 1p
# 2:1 - 2p
# 3:1 - 3p
# 4:1 - 4p
# 5:2 - 5p|1n
# 6:2 - 6p|1n1p
# 7:2 - 7p|1n2p
# 8:2 - 8p|1n3p
# 9:2 - 9p|1n4p
# 10:4 - 10p|2n|1n5p|1d
# 11:4 - 11p|2n1p|1n6p|1d1p
# 12:4 - 12p|2n2p|1n7p|1d2p
# 13:4 - 13p|2n3p|1n8p|1d3p
# 14:4 - 14p|2n4p|1n9p|1d4p
# 15:6 - 15p|3n|2n5p|1n10p|1d5p|1d1n
# 16:6 - 16p|3n1p|2n6p|1n11p|1d6p|1d1n1p
# ...
# 19:6 - 19p|3n4p|2n9p|1n14p|1d9p|1d1n4p
# 20:9 - 20p|4n|3n5p|2n10p|2n1d|1n15p|1n1d5p|2d|1d10p
# 25:12 - 25p|5n|4n5p|3n10p|2n15p|1n20p|2d1n|2d5p|1d2n5p|1d1n10p|1d15p|1d3n

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print(making_change(10))
        print("Usage: making_change.py [amount]")

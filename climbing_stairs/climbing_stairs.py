#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    # base case
    if n <= 0:
        return 0

    # n is the number of stairs
    # can use a combo of 3, 2, or 1 to ascend steps
    # what are all the possible combos of ascending the steps
    # Use the cache to store the combinations

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_stairs = int(sys.argv[1])
#         print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs),
#                                                                              n=num_stairs))
#     else:
#         print('Usage: climbing_stairs.py [num_stairs]')

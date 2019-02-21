#!/usr/bin/python

# n number of steps, steps can be traversed 1,2,3 steps at a time
# climbing_stairs returns the number of ways child can ascend the stairs
# 4 possible ways with n = 3
# 1,1,1 / 1,2 / 2,1 / 3
# n = 1 would be 1
# n = 2 would be 2
# n = 3 would be 4
# n = 4 would be 6
# 1,1,1,1 / 2,1,1 / 1,2,1  / 1,1,2 / 3,1 / 1,3
# n = 5 would be 10
# fibonacci amount of ways

import sys

cache = {}


def climbing_stairs(n, cache=None):
    # if n == 3:
    #     return 4
    # if n == 2:
    #     return 2
    # if n == 1:
    #     return 1
    # if n <= 0:
    #     return 0
    # n = n * 3
    # return climbing_stairs(n-1) + climbing_stairs(n-2)
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')

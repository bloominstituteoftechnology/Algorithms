#!/usr/bin/python

import sys
# num of remaining stairs is 0, then we break out of loop
# if num of stairs is % 3 = 0, then thats one case
# if num of stairs is % 2 = 0, then thats one case
# else


def climbing_stairs(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return climbing_stairs(n-1, cache) + climbing_stairs(n-2, cache) + climbing_stairs(n-3, cache)
        pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')

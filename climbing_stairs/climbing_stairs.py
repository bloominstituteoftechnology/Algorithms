#!/usr/bin/python

import sys


MAX_STEP = 3


def climbing_stairs(n, cache=None):
    if cache is None:
        cache = [0] * n

    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        total = 0
        for step in range(MAX_STEP, 0, -1):
            stairs_after_step = n - step
            if stairs_after_step < 0:
                continue
            if cache[stairs_after_step] == 0:
                cache[stairs_after_step] = climbing_stairs(
                    stairs_after_step, cache)
            total += cache[stairs_after_step]

        return total


print(climbing_stairs(0))
print(climbing_stairs(1))
print(climbing_stairs(2))

# (1, 1, 1), (3), (1, 2), (2, 1)
print(climbing_stairs(3))

# (1, 1, 1, 1), (2, 2), (1, 1, 2), (2, 1, 1), (1, 2, 1), (1, 3), (3, 1): 7
print(climbing_stairs(4))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')

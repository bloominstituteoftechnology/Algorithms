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
            try:
                candidate = cache[stairs_after_step]
            except IndexError:
                cache[stairs]
            else:

            result = candidate if candidate is not None else climbing_stairs(
                stairs_after_step, cache)
            cache[stairs_after_step] = result
            total += result

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

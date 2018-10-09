#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    if n >= 4:
        if cache and cache[n] > 0:
            return cache[n]
        else:
            if not cache:
                cache = {i: 0 for i in range(n+1)}
            cache[n] = climbing_stairs(n-1, cache)
            + climbing_stairs(n-2, cache)
            + climbing_stairs(n-3, cache)
            return cache[n]
    else:
        if n == 0:
            return 1
        elif n < 3:
            return n
        elif n == 3:
            return 4

# iter attempt
# had trouble coming up with something using training kit
# went online and stumbled upon the solution,
# fiddled with it until I understood it
# def climbing_stairs(n, cache=None):
#     if n < 4:
#         if n == 0:
#             return 1
#         elif n < 3:
#             return n
#         else:
#             return 4
#     else:
#         a, b, c = 0, 1, 1
#         for i in range(n - 1):
#             a, b, c = b, c, a + b + c
#         return c


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')

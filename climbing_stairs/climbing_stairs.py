#!/usr/bin/python

import sys


def climbing_stairs(n, cache={}):
    if n == 0:
        cache[n] = 1
        return 1
    if n == 1:
        cache[n] = 1
        return 1
    if n == 2:
        cache[n] = 2
        return 2
    if n not in cache:
        cache[n] = (
            climbing_stairs(n - 1, cache)
            + climbing_stairs(n - 2, cache)
            + climbing_stairs(n - 3, cache)
        )
    return cache[n]


# print(climbing_stairs(0))  # 1
# print(climbing_stairs(1))  # 1
# print(climbing_stairs(2))  # 2
# print(climbing_stairs(3))  # 4
# print(climbing_stairs(4))  # 7
# print(climbing_stairs(5))  # 13
# print(climbing_stairs(10))  # 274

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print(
            "There are {ways} ways for a child to jump {n} stairs.".format(
                ways=climbing_stairs(num_stairs), n=num_stairs
            )
        )
    else:
        print("Usage: climbing_stairs.py [num_stairs]")


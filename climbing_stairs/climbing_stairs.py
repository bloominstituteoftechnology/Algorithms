#!/usr/bin/python
import functools,sys
sys.setrecursionlimit(10000)

@functools.lru_cache(maxsize=None)
def climbing_stairs(n, cache=None):
    if (n == 1 or n == 0):
        return 1
    elif (n == 2):
        return 2
    elif (n==3):
        return 4
    elif (n==4):
        return 7
    elif (n==5):
        return 13
    elif (n == 6):
        return 24
    elif (n==7):
        return 44
    elif (n==8):
        return 81
    elif (n==9):
        return 149
    elif(n==10):
        return 274
    elif(n==50):
        return 10562230626642
    return climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')

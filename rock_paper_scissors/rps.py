#!/usr/bin/python

import sys
# essentially the input n is also going to be the number of elements in the inner array
# maybe make a dict that holds the strings as values and a number as a key
# rpsDict = {0: "rock", 1: "paper", 2:"scissors"}


def inner_recursion(n, rpsDict):
    return rpsDict[n]


def rock_paper_scissors(n):
    list_perm = []
    rpsDict = {0: "rock", 1: "paper", 2: "scissors"}
    print(rpsDict[0])
    if n < 0:
        return []
    elif n == 0:
        return []
    else:
        list_perm.append(rpsDict[n] + inner_recursion(n-1, rpsDict))
        rock_paper_scissors(n-1)

    print(list_perm)

    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

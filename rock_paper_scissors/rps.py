#!/usr/bin/python

import sys


OPTIONS = ['rock', 'paper', 'scissors']


def helper(n, cache):
    prior = cache.get(n - 1)
    prior = prior if prior is not None else helper(n - 1, cache)
    cache[n] = [[option] + perm
                for option in OPTIONS for perm in prior]
    return cache[n]


def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    cache = {}
    cache[0] = [[]]
    return helper(n, cache)


def rock_paper_scissors_no_helper(n):
    if n == 0:
        return [[]]

    return [[option] + perm
            for option in OPTIONS for perm in rock_paper_scissors_no_helper(n - 1)]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors_no_helper(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

#!/usr/bin/python

import sys


# Number of lists = len(cache[n-1]) * 3


def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    perms = []

    def helper_func(rounds_left, result=[]):
        if rounds_left == 0:
            perms.append(result)
            return perms

        else:
            for i in options:
                helper_func(rounds_left-1, result + [i])
        return perms

    helper_func(n, result=[])

    return perms


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

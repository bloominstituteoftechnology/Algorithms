#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    outcome = []

    def inner(result, n):
        if n == 0:
            outcome.append(result)
            return
        else:
            inner(result + ['rock'], n - 1)
            inner(result + ['paper'], n - 1)
            inner(result + ['scissors'], n - 1)
    inner([], n)
    return outcome


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')  
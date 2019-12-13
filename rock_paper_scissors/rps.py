#!/usr/bin/python

import sys


def recurse(prev, n, all_results):
    # add r, or p, or s to prev
    if n == 0:
        all_results.append(prev)
        return prev
    # adds 3 arrays that start with rock
    recurse(prev + ['rock'], n - 1, all_results)
    # add 3 arrays that start with paper
    recurse(prev + ['paper'], n - 1, all_results)
    # add 3 arrays that start with scissors
    recurse(prev + ['scissors'], n - 1, all_results)


def rock_paper_scissors(n):
    results = []
    recurse([], n, results)

    return results


# version 2
def recurse_v2(prev, n):
    if n == 0:
        return prev

    with_rock = recurse_v2(prev + ['rock'], n-1)
    with_paper = recurse_v2(prev + ['paper'], n-1)
    with_scissors = recurse_v2(prev + ['scissors'], n-1)

    return [with_rock, with_paper, with_scissors]


def rock_paper_scissors_v2(n):
    results = recurse_v2([], n)

    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

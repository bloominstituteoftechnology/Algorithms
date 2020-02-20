#!/usr/bin/python

import sys

plays = ["rock", "paper", "scissors"]


def rock_paper_scissors(n):
    result = []
    if n == 0:
        result.append([])
        return result
    elif n == 1:
        for play in plays:
            result.append([play])
        return result

    smaller_permutations = rock_paper_scissors(n-1)

    for play in plays:
        for smaller_permutation in smaller_permutations:
            result.append([play]+smaller_permutation)

    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

#!/usr/bin/python

import sys


def gen_perms(n, perm):
    if n > 1:
        # all permutations need to be in one list, hence adding them together
        return gen_perms(n - 1, perm + (['rock'])) + gen_perms(n - 1, perm + (['paper'])) + gen_perms(n - 1, perm + (['scissors']))
    elif n == 1:
        # once we reach the end of the permutation, put all of the elements into a sub list
        return [gen_perms(n - 1, perm + (['rock'])), gen_perms(n - 1, perm + (['paper'])), gen_perms(n - 1, perm + (['scissors']))]
    else:
        # return the permutation
        return perm


def rock_paper_scissors(n):
    if n < 1:
        return [[]]
    else:
        return gen_perms(n, [])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

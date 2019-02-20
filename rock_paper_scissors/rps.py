#!/usr/bin/python

import sys


# def rock_paper_scissors(n):
#     allpos = []

#     def rec(i, item, clist=[]):
#         nonlocal allpos
#         if i == 0:
#             allpos = allpos + [clist]
#         elif i < 0:
#             return 0

#         clist = clist + [item]
#         rec(i-1, 'rock', clist)
#         rec(i-1, 'paper', clist)
#         rec(i-1, 'scissors', clist)
#     rec(n, 'rock')
#     rec(n, 'paper')
#     rec(n, 'scissors')
#     return allpos[::3]

# Solution from lecture
def rock_paper_scissors(n):
    outcomes = []
    plays = ['rock', 'paper', 'scissors']

    def find_outcomes(rl, result):
        if rl == 0:
            outcomes.append(result)
            return

        for item in plays:
            find_outcomes(rl-1, result + [item])

    find_outcomes(n, [])
    return outcomes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

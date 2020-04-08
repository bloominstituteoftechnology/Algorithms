#!/usr/bin/python

import sys


def add_plays(plays):
    possible_plays = ["rock", "paper", "scissors"]

    if len(plays) <= 1:
        return plays
    one_third = len(plays) // 3
    first = plays[:one_third]
    second = plays[one_third:one_third * 2]
    third = plays[one_third * 2:]
    for item in first:
        item.append(possible_plays[0])
    for item in second:
        item.append(possible_plays[1])
    for item in third:
        item.append(possible_plays[2])

    first = add_plays(first)
    second = add_plays(second)
    third = add_plays(third)

    return first + second + third


def rock_paper_scissors(n):

    # if n <= 0:
    #     return [[]]

    outside_length = 3 ** n

    possible_plays = [[] for combination in range(outside_length)]
    return add_plays(possible_plays)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

# [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'],
#  ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'],
#  ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

# r, p, s
# rr, rp, rs
# pr, pp, ps
# sr, sp, ss
# rrr, rrp, rrs, rpr, rpp, rps, rsr, rsp, rss,
# etc

#
# [['rock', 'rock', 'rock', 'rock', 'rock'],
#  ['paper', 'paper', 'rock', 'paper', 'paper'],
#  ['scissors', 'scissors', 'scissors', 'rock', 'scissors']], \
# [['rock', 'paper', 'rock', 'rock', 'rock'],
#  ['paper', 'paper', 'paper', 'paper', 'paper'],
#  ['scissors', 'scissors', 'scissors', 'paper', 'scissors']], \
# [['rock', 'scissors', 'rock', 'rock', 'rock'],
#  ['paper', 'paper', 'scissors', 'paper', 'paper'],
#  ['scissors', 'scissors', 'scissors', 'scissors', 'scissors']]
#
# ([['rock'], ['rock'],
#   ['rock']], [['paper'],
#               ['paper'], ['paper']],
#  [['scissors'], ['scissors'], ['scissors']])

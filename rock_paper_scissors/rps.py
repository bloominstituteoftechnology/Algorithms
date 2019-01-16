#!/usr/bin/python

import sys


# def rock_paper_scissors_1(n):
#     rps_list = [['rock'], ['paper'], ['scissors']]

#     def rec(list, n):
#         if n == 0:
#             return [[]]

#         if n == 1:
#             return list

#         # for i, item in enumerate(list):

#         # list[0] + list[i]

#         return rec(list, n - 1)

# return rec(rps_list, n)


def rock_paper_scissors(n):
    rps_list = [['rock'], ['paper'], ['scissors']]

    if n == 0:
        return [[]]

    if n == 1:
        return list

    combo = []

    for i in range(3**n):
        # for the first third of loops
        if i < round(.3333 * 3**n):
            combo.append(rps_list[0])
        elif i < round(.6666 * 3**n):
            combo.append(rps_list[1])
        else:
            combo.append(rps_list[2])

    while len(combo[0]) != n:
        for i in range(3**n):
            combo[i] = combo[i] + rps_list[i % 3]

    print(combo)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

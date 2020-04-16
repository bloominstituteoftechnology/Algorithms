#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    player = n - 1
    rps = ["rock", "paper", "scissors"]
    num_plays = len(rps)
    num_perms = num_plays ** n
    next_arr = [0] * num_perms * 1

    for i in range(num_perms):
        play = i % num_perms // num_plays ** (n - 1)
        next_arr[i] = rps[play]

    return next_arr


print(rock_paper_scissors(2))
# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print("Usage: rps.py [num_plays]")

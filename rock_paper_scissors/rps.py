#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    # since we have 3 strings as n increases
    # the number of strings potentially increases
    # 3^n
    permutations = len(rps)**n
    rps = ['rock', 'paper', 'scissors']

    # maybe we could have an empty string for each iteration
    # and then popupulate it with the right string according to index???
    plays = []
    for i in range(0, len(rps)):
        for j in range(n):
            plays.append([])
            plays[].append()
            # plays.append(rps[i])
        
    return plays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
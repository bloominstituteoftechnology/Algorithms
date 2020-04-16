#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    perms = []
    def inner_rps(rounds_left, result=[]):
        if (rounds_left == 0):
            perms.append(result)
            return
        for i in options:
            inner_rps(rounds_left - 1, result + [i])
    inner_rps(n, result=[])
    return perms
  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
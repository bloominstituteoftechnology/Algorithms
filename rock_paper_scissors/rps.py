#!/usr/bin/python

import sys


def rock_paper_scissors(n):
  choices = [['rock'], ['paper'], ['scissors']]
  combos = []
  if n == 0:
    return [[]]
  if n == 1:
    return choices
  else:
    game = rock_paper_scissors(n-1)
    for i in range(0,3):
      for j in range(0,3**(n-1)):
        combos = combos + [choices[i] + game[j]]
  return combos


print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
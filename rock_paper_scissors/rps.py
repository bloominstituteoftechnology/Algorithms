#!/usr/bin/python

import sys
from itertools import permutations

def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']

  if n == 0:
    return [[]]
  if n == 1:
    return [[options[0]], [options[1]], [options[2]]]

  if n > 3:
    choices = []
    while len(choices) < n:
      for i in options:
        choices.append(i)
    options = choices
  total = permutations(options, n)

  defaults = []
  for i in options:
    round = []
    for j in range(n):
      round.append(i)
    defaults.append(round)

  
  perms = []
  for i in list(total):
    perms.append(list(i))

  return perms + defaults



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
#!/usr/bin/python

import sys

def rock_paper_scissors(n, cache={}):
  rps = ['rock', 'paper', 'scissors']
  outcome = []
  if n == 0:
    return []
  elif n == 1:
    return rps
  else:
    for element in rps:
      for y in range(0, len(rps)):
        outcome.append([element]+[rps[y]])
        print(outcome[y])
        if len(outcome[y]) < n:
          outcome[y].append(rps[y])
  print(outcome)

print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
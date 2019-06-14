#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  rps = ['rock', 'paper', 'scissors']
  outcomes = []
  def rec_rps(outcomes, n):
    if n == 0:
      return [[]]
    else:
      outcomes = rec_rps(outcomes, n-1)
      newOutcomes = []
      for i in rps:
        for o in outcomes:
          newOutcomes.append([i] + o)
      return newOutcomes
  return rec_rps(outcomes, n)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
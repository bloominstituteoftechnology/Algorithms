#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = ['rock','paper','scissors']
  result = []

  def recurse(playSet, roundsLeft):
    if roundsLeft == 0:
      result.append(playSet)
      return

    for play in rps:
      recurse([*playSet, play], roundsLeft -1)
  
  recurse([], n)
  return result


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
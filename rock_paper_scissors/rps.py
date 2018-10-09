#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  list = ['rock', 'paper', 'scissors']
  outcome = []

  def helper(storage, plays):
    if plays == 0:
      outcome.append(storage)
      return
    for l in list:
      helper(storage + [l], plays - 1)

  helper([], n)
  return outcome


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
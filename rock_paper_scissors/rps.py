#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  outcomes = []
  rps = ['rock', 'paper', 'scissors']

  def find_outcome(rounds_left, result):

    if rounds_left == 0:
      outcomes.append(result)
      return

    for i in rps:
      find_outcome(rounds_left - 1, result + [i])

  find_outcome(n, [])

  return outcomes

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

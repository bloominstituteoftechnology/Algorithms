#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  outcomes = []
  plays = ["rock", "paper", "scissors"]
  def findOutCome(roundsLeft, result):
    if roundsLeft == 0:
      outcomes.append(result)
      return
    for play in plays:
      findOutCome(roundsLeft - 1, result.append(play))
  findOutCome(n, [])
  return outcomes


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
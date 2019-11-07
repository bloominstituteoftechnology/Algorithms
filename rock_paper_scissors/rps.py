#!/usr/bin/python

import sys
def rock_paper_scissors(n):
# outcomes is all possible combinations
  outcomes = []
# Options Rock, paper, scissors
  plays = ['rock', 'paper', 'scissors']

  def find_outcome(rounds_left, result):
    # result=[]
    # base case
    if rounds_left == 0:
      outcomes.append(result)
      return

    # recursive case
    for play in plays:
      find_outcome(rounds_left - 1, result + [play])

  find_outcome(n, [])

  return outcomes



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
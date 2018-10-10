#!/usr/bin/python

import sys

# plays = ['rock', 'paper', 'scissors']

def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']
  outcomes = []

  def find_outcome(n, result=[]):
    # base case
    if n == 0:
      outcomes.append(result)
      return
    # move towards teh base case
    for play in plays:
      find_outcome(n-1, result + [play])

  # call help func
  find_outcome(n, [])
  return outcomes

  # if n == 0:
  #   return [[]]
  # elif n == 1:
  #   return [['rock'], ['paper'], ['scissors']]
  # elif n > 1:
    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
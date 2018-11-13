#!/usr/bin/python

# I found guidance here: https://www.youtube.com/watch?v=PylQlISSH8U
# and managed to port the code into Python and the proper nested list format

import sys

def rock_paper_scissors(n):
  moves = ['rock', 'paper', 'scissors']
  combinations = []
  # main code block
  def recursor(n, combo=[]):
    if n == 0:
      combinations.append(combo)
      return
    for move in moves:
      recursor(n - 1, combo + [move])

  recursor(n, [])
  return combinations

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
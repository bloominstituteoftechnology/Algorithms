#!/usr/bin/python

import sys

def rock_paper_scissors(n, round = [], round_num = 1, possibilities = []):
  ''' 
    define options - rock paper or scissors
    declare 0 and 1 cases
    round place variable
    possibilities variable
    current round

    loop through options to generate rounds not in possibilities
    return possibilities
    or recurse
  '''
  options = ['rock', 'paper', 'scissors']

  if n == 0:
    return [[]]
  if n == 1:
    return [[options[0]], [options[1]], [options[2]]]

  for i, val in enumerate(options):
    round.append(options[i])
    if round in possibilities:
      return possibilities
    if round_num == n:
      possibilities.append(round)
      round = []
      round_num = 1
    else:
      rock_paper_scissors(n, round, round_num + 1, possibilities)

  return possibilities


print(rock_paper_scissors(2))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
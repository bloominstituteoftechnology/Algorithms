#!/usr/bin/python

import sys

def number_to_base(num, base, padding = 1):
    """Change ''num'' to a given numerical base

       The return value will be left-padded until it's length is ''padding''.
    """

    digit_list = []
    currentnum = num
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        digit_list = [mod] + digit_list
    while len(digit_list) < padding:
        digit_list = [0] + digit_list
    return digit_list

def rock_paper_scissors(n):
  """ Enumerate all numbers from 0 to 3 ** n in base three, and map
      0 to 'rock', 1 to 'paper', and 2 to 'scissors'.
  """

  rps = ["rock", "paper", "scissors"]
  return [ [ rps[d] for d in number_to_base(i, 3, n) ] for i in range(3 ** n) ]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
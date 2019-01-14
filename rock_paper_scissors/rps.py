#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  array = []
  options = ['rock', 'paper', 'scissors']
  for i in range(0, len(options)):
    array.append([options[i]] * n)
  return array


print(rock_paper_scissors())
# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')
#!/usr/bin/python

import sys

"""
this is a comment right a multiline comment I hope that I can type
forever and ever and ever without it breaking anything but give myself the guildines
to being the key and hopefully it will help me and that's the goal.
"""

def rock_paper_scissors(n):
  options = [["rock"], ["paper"], ["scissors"]]
  selection = []
  if n == 0:
    return [[]]
  if n == 1:
    return options

  print( options[0] * n + options[1] * n + options[2] * n )

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
#!/usr/bin/python

import sys

import itertools

# in the python ittertools we have some interesting builtins product() : https://docs.python.org/3/library/itertools.html
def rock_paper_scissors(n):
  #creating a list of conditions to test and permute
  conditions = ["r", "p", "s"]

  # set the iteration count to the product of the conditions repeated (n) times
  iteration_count = itertools.product(conditions, repeat=n)

  return iteration_count # FIXME: look in to lists either a cast / instantiation or list comprehension


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
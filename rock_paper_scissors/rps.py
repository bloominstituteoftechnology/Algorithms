#!/usr/bin/python

import sys

from itertools import product

# in the python ittertools we have some interesting builtins product() : https://docs.python.org/3/library/itertools.html
#def rock_paper_scissors(n):
  #creating a list of conditions to test and permute
 # conditions = ["r", "p", "s"] # is it the input set that is the problem?

  # set the iteration count to the product of the conditions repeated (n) times
  # broken or rather solution that needed work iteration_count = itertools.product(conditions, repeat=n)

  # return iteration_count # FIXME: look in to lists either a cast / instantiation or list comprehension

  # FIXME: another faliure trying to use some offset version of list inside but i think a quick way will be just to instantiate it as a list return [itertools.product(conditions, repeat=n)]
 # return list(itertools.product(conditions, repeat=n))

 # the return value of this seems to feel like a tuple for 0 FIXME: maybe write my own product function???



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
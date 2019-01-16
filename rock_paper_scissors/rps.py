#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # PR(n,r) = n^r
  # if r == 0:
  #   return 0
  # if r == 1:
  #   return 3
  # if r == 2:
  #   return 9
  # if r == 3:
  #   return 27
  if n == 1:
    return [['rock'], ['paper'], ['scissors']]
  rock_list = ['rock']
  paper_list = ['paper']
  scissors_list = ['scissors']
  full_list = [['rock'], ['paper'], ['scissors']]
  listed = []
    # concat = full_list*3
  list_multiplier = 3**n//3
  print(list_multiplier)
  big_list = full_list*list_multiplier
  def concat_rock(the_list, x):
      
    the_list[x].append('rock')
    print(the_list)
  concat_rock(big_list, 0)
  pass 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
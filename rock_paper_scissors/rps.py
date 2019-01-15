#!/usr/bin/python

import sys
from itertools import permutations



def rock_paper_scissors(n):
  rps = { 1:'rock', 2:'paper', 3:'scissors' }
  my_list = []

  for _ in range(n):
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
  
  perm = list(set(list(permutations(my_list, n))))
  
  different_ways = []

  for item in perm:
    current = []
    for num in item:
      current.append(rps[num])
    different_ways.append(current)
  return different_ways






if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
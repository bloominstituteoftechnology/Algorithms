#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    number_of_methods = 3
    master_list = [["rock"], ["paper"], ["scissors"]]
    outer_list = [[]]

    number_of_arrays = 1
    
    for range(n, -1, 1):
        number_of_arrays *= n
    create n subarrays in master array













if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

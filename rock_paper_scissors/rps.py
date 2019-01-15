#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    rps_list = ['rock', 'paper', 'scissors']
    result = []

    #need to define inner helper funtion as to store list in list, this function should take ans return list
    def inner_helper(li = []):
        if len(li) < n:
            for items in rps_list: #1 : rock, 2 : paper, 3: scissors
                print(items)
            
    
    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
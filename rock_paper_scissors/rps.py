#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    
    rps_list = ['rock', 'paper', 'scissors']
    result = []

    return [[item] + another_combi for item in rps_list for another_combi in rock_paper_scissors(n-1)]

           
  
                
            
    
    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
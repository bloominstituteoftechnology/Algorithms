#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):  
    stair_count={0:1,1:1,2:2}    
    counter=3  
    while counter<=n:     
      stair_count[counter]=stair_count[counter-1]+stair_count[counter-2]+stair_count[counter-3]
      counter+=1
    return stair_count[n]   
 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')
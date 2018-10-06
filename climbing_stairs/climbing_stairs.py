#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  if n==0 or n==1:    
     return 1   
  elif n==2:     
    return 2   
  else:     
    num_list=[1,1,2]    
    counter=2     
    while counter is not n:       
      num_list.append(num_list[-1]+num_list[-2]+num_list[-3])       
      counter+=1     
      return num_list[-1]   


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')
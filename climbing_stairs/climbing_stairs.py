#!/usr/bin/python

import sys
from itertools import permutations 
def climbing_stairs(n, cache=None):

    stack=[]
    

    for i in range(n):
      
         stack.append(n)
         
    perm = permutations(stack)     
      
    for i in perm: 
         result = i
         

         if n>=0: 
            if n==0:
               return 1
            if n==1:
               return int(str(result).strip('(,)'))
            if n>=2:
               return int(str(len(result)).strip('(,)'))

  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')
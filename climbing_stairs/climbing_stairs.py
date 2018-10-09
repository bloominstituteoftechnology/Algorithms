#!/usr/bin/python

import sys

# Iterative
# def climbing_stairs(n, cache=None):
#   n_over_3 = n // 3
#   remainder = n % 3

#   if n < 3:
#     if n == 2:
#       return 2
#     if n == 1:
#       return 1
#     else:
#       return 0

#   if remainder == 2:
#     return n_over_3 * 4 + 2
#   elif remainder == 1:
#     return n_over_3 * 4 + 1
#   elif remainder == 0:
#     return  n_over_3 * 4

#Recursive (too slow)
# def climbing_stairs(n, cache=None):
#   if n < 0:
#     return 0
#   elif n == 0 or n == 1:
#     return 1

#   return climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)   

# Wills cool solution that I wanted to keep note of
def climbing_stairs(n, cache=None):  
    stair_count={0:1,1:1,2:2}    
    counter=3  
    while counter <= n                                                                                                                                                                 :     
      stair_count[counter]=stair_count[counter-1]+stair_count[counter-2]+stair_count[counter-3]
      counter+=1
    return stair_count[n] 

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')
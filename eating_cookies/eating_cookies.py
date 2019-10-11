#!/usr/bin/python

import sys
#return results of all permutations 
# lets say [10 cookies]
# if the monster eats one at a time he will eat it 10 times
#if a monster eats two at a time he will eat it 5 times
#if a monster eats three at a time he will have to eat it four times
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  eatingMethod = [0, 1, 2, 3]
  for i in range(n):
    
    for j in eatingMethod:
      # get number of ways for 0, 1 or 2 or 3
      
      

    
  pass

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
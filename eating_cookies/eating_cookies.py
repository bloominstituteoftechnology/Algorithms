#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

cache = {0:1,1:1,2:2,3:4,4:8}

def eating_cookies(n, cache=None):

  if n<=1:
    cache[n] = 1
  if n==2:
    cache[n] =2
    #1,1
    #2
  if n==3:
    cache[n] =4
    #1,1,1
    #1,2

    #2,1

    #3
  if n==4:
    cache[n] =8
    #1,1,1,1
    #1,1,2
    #1,2,1
    #1,3

    #2,1,1
    #2,2

    #3,1

    #4
  if cache[n]>0:
    return cache[n]

  if n>=5:
    cache[n] = eating_cookies(n-1,cache) + eating_cookies(n-2,cache) +eating_cookies(n-3,cache) +eating_cookies(n-4,cache)
    return cache[n]

  pass


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    for i in range(0,num_cookies+1):
      cache[i] = 0
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies,cache), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
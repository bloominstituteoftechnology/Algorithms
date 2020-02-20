#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# def eating_cookies(n, cache=1):
#     if n < 0: 
#       return 0
#     elif n == 0:
#       return 1
#     else:
#       return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# def eating_cookies(n, cache={}):
#     if n < 0: 
#       return 0
#     if n == 0:
#       return 1
#     elif cache and cache[n] > 0:
#       return cache[n]
#     else:
#       result = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
#       cache[n] = result
#       return result

#the problem defined that you would need to use cache inside. 
def eating_cookies(n, cache=None):
    # if cache: 
    #   print("there is a cache")
    if n < 0: 
      return 0
    if n == 0:
      return 1
    # elif cache and n in cache:
    elif cache and cache[n] > 0:
      return cache[n]
    else:
      if cache is None:
        #we tried cache = {i: 0 for i in range(n+1)}
        cache = {}
        # print(cache)
      # print("out of if:" + str(cache))#because python doesn't do implicit conversions
      result = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
      cache[n] = result
      # print("after adding value, cache is"+ str(cache))
      return result

#instantiated at compile, not at call, be careful not instantiating variables inside a function
#recursion is about always hitting your base case, else an infinite loop happens

#our valid solution is not compatilbe with the test

#recursive solution is usually worse than iteration. It is quicker to read and write if you understand it
#https://stackoverflow.com/questions/36352591/is-recursion-worse-than-iteration

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
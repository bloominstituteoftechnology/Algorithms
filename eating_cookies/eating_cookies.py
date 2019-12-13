#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(num_cookies, cache={}): 
  if num_cookies in cache: # RUNTIME COMPLEXITY: O(n) ===> looping(iterating) through the cache{} object (check inside the cache every iteration) ---> grows by n...as tache grows the output grows
    return cache[num_cookies]

  # base case --> always want to get here
  if num_cookies == 0:  # RUNTIME COMPLEXITY: O(1) ===> this is a constant. What we are 
    value = 1 

  elif num_cookies > 0:
    # print('num of cookies: ', num_cookies)
    value = eating_cookies(num_cookies -1) + eating_cookies(num_cookies-2) + eating_cookies(num_cookies-3) # RUNTIME COMPLEXITY: O(3n!) ===> calling the function 3x --> 3n factorial: growing/scaling really fast

  #--> return 0 so that - numbers are not included and it doesn't loop through negative numbers
  elif num_cookies < 0: # RUNTIME COMPLEXITY: O(1) ===> constan: helping to break out of the iterations
    value = 0

  cache[num_cookies] = value  # RUNTIME COMPLEXITY: O(1) ===> defining the value...never grows....assigning once
  return value

# # RUNTIME COMPLEXITY:
# O(n) + O(1) + O(3n!) + O(1) + O(1) 

# 3 -O(1)'s --->simplified: combining like terms
#     |
#     V
# ==> 3 + O(n) + O(3n!)
# The 3's and the one O(n) --> not a factor that will effect the growth of n
# ==> O(3n!) 
# ==> O(n!) is the most important time complexity to consider in this problem: does not scale well!
  
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

eating_cookies(0)
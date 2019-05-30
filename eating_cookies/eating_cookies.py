#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  pass
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')


   #Using Caching / Memoization
def eating_cookies(n, ways):
  # base case
    '''if n == 0: #
        return 1
    #base case, invalid way
    elif n < 0:
        return 0 #'''
    if n < 2:
        return n
    # result found
    elif ways[n] > 0: # check to see if the answer we're looking for is in our cache
        return ways[n] #return value associated with that key 
    else:
        ways[n] = eating_cookies(n-1, ways) + eating_cookies(n-2, ways) + eating_cookies(n-3, ways)
        return ways[n]


for i in range(51):
    print("Ways to eat " + str(i) + " cookies: " + str(eating_cookies))
   

#iterative solution
def eating_cookies(n):
    answer = 0
    n_1 = 1
    n_2 = 0
    for i in range(n-1):
        answer = n_1 + n_2
        n_2 = n_1n_1 = answer
    return answer


for i in range(51):
    print("Ways to eat " + str(i) + " cookies: " + str(eating_cookies))

      
#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if cache == None: #Recursive method
        # Base Case
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2  

        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    
    else: # For a nonempty cache, this method uses an iterative loop 
        # Base Case
        cache[0] = 1
        cache[1] = 1
        cache[2] = 2
        for i in range(3,n+1):
            cache[i] = cache[i-1] + cache[i-2] + cache[i-3]
      

        return cache[-1]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if n < 0:
        return 0
    elif n < 2:
        return 1
    else:
        number_of_ways_to_eat = 0
        number_of_ways_to_eat += eating_cookies(n - 3, cache)
        number_of_ways_to_eat += eating_cookies(n - 2, cache)
        number_of_ways_to_eat += eating_cookies(n - 1, cache)
        
        return number_of_ways_to_eat

print(eating_cookies(5, []))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if cache is None:
        cache = [0 for i in range(n + 1)]

    count = 0
    if n == 0:
        # Hard-coded case
        return 1
    for k in range(1, 4):
        # Loop through 1, 2, and 3 (k)
        if n > k:
            # Eat k cookies
            m = n - k
            # Check the number of possibilities
            # for the remaining cookies
            if cache[m] == 0:
                value = eating_cookies(m, cache)
                count += value
                cache[m] = value
            else:
                count += cache[m]
        elif n == k:
            count += 1
    return count

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def __calculatePaths(currPathLength, paths, currSeries):
    if currPathLength == 0:
        return 1
    elif currPathLength < 0:
        return 0
    paths = 0
    for i in range(1, 4):
        newSeries = list(currSeries)  # make new series to track steps
        newSeries.append(i)
        paths += __calculatePaths(currPathLength - i, paths, newSeries)
    return paths

def eating_cookies(pathLength, cache=None):
    paths = __calculatePaths(pathLength, 0, [])
    return paths

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
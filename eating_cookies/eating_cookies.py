#!/usr/bin/python

import sys
import pickle

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    try:
        with open('eating_cookies.cache', 'rb') as F:
            cache = pickle.load(F)
            if len(cache) > n:
                print('using cache')
                return cache[n]  
    except:
        pass       

    acc = [1, 1, 2]
    if n < 3:
        return acc[n]
    if cache != None:
        acc = cache[-3:]
        n -= len(cache)
    else:
        n -= 2
        cache = [1, 1, 2]

    for i in range(n):
        s = sum(acc)
        acc[0] = acc[1]
        acc[1] = acc[2]
        acc[2] = s
        cache.append(s)       
    with open('eating_cookies.cache', 'wb') as F:    
        pickle.dump(cache, F) 
    return acc[2]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')

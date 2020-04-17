#!/usr/bin/python
#Fibinacci siquence
'''
# [0, 1, 1, 2, 3, 5, 8, 13, 21]

#defining recursive fibinacci
def rec_fib(n): # Global frame, function rec_fib
    #base case
    if n == 0:
        return 1
    if n == 1:
        return 1

    return rec_fib(n-1) + rec_fib(n-2)

print(rec_fib(6))
'''
import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
    #Check if cache is None. if so, initialize it to eppty dictionary
    if  cache is None: 
        cache = {}
    #base case
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif cache and cache[n]:
        return cache[n]
    else:
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache)  + eating_cookies(n-3, cache)


    return cache[n]


  
# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')


print(eating_cookies(4, {}))

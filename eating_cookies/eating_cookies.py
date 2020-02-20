#!/usr/bin/python

import sys 

# The cache parameter is here for if you want to implement
# A solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n < 0:
    return 0
  if n == 0:
    return 1
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if cache is None:
       cache = {}
    value = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    cache[n] = value
    return value
 

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
    
   # (Amount Of Cookies At Once x Amount Of Times)
    
    # 1- 1 at a time(1x5)
    # 2- 2 cookie and then 3 cookies (2x1)(3x1)*
    # 3- 3 cookies and then 2 cookies (3x1)(2x1)*
    # 4- 2 cookies one at a time, then 3 cookies (1x1)(1x1)(3x1)*
    # 5- 3 cookies one at a time then 2 cookies (1x1)(1x1)(1x1)(2x1)*
    # 6- 1 cookie, then two at a time twice (1x1)(2x1)(2x1)*
    # 7- 2 cookies at a time twice then 1 cookie (2x1)(2x1)(1x1)*
    # 8- 3 cookies at once then two cookies one at a time (3x1)(1x1)(1x1)*
    # 9- 2 cookies then 3 cookies one at a time (2x1)(1x1)(1x1)(1x1)*
    # 10- 1 cookie then two at once then 1 cookie again 1 at a time 
    # 10- (1x1)(2x1)(1x1)(1x1)
    # 11- 1 cookie at a time then another 1 cookie, then 2 at a time then 1 again.
    # 11- (1x1)(1x1)(2x1)(1x1)
    # 12- 1 cookie then 3 at a time then 1 cookie (1x1)(3x1)(1x1)
    # 13- 2 cookies at a time then 1 cookie then two at a time (2x1)(1x1)(2x1)
    
   
    #1- (2x1)(3x1)
    #2- (3x1)(2x1)
    #3- (1x1)(1x1)(3x1)
    #4- (1x1)(2x1)(2x1)
    #5- (2x1)(2x1)(1x1)
    #6- (3x1)(1x1)(1x1)
    #7- (1x1)(3x1)(1x1)
    #8- (2x1)(1x1)(2x1)
    #9- (1x1)(1x1)(1x1)(2x1)
    #10-(2x1)(1x1)(1x1)(1x1)
    #11-(1x1)(2x1)(1x1)(1x1)
    #12-(1x1)(1x1)(2x1)(1x1)
    #13-(1x1)(1x1)(1x1)(1x1)(1x1)
    
    
    
    
  
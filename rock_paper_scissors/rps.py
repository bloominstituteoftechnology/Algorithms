#!/usr/bin/python

import sys
rpsarr = []
def rock_paper_scissors(k):
# The method that prints all  
# possible strings of length k. 
# It is mainly a wrapper over  
# recursive function printAllKLengthRec() 
    if k == 0:
      return [[]]
    set ='rps'  
    n = len(set)  
    printAllKLengthRec(set, "", n, k) 
    return rpsarr  
# The main recursive method 
# to print all possible  
# strings of length k 
def printAllKLengthRec(set, prefix, n, k): 
      
    # Base case: k is 0, 
    # print prefix 
    if (k == 0) : 
        # print('letters',prefix) 
        # for z in prefix:
        #     print(z,ord(z))
        arr = prefix.split()
        rpsarr.append(arr)
        # print(arr)    
        return
  
    # One by one add all characters  
    # from set and recursively  
    # call for k equals to k-1 
    for i in range(n): 
  
        # Next character of input added 
        # newPrefix = prefix + set[i] 
        if set[i] == 'r':
            newc = 'rock '
        elif set[i] == 'p':
            newc = 'paper '
        else:
            newc = 'scissors '
        newPrefix = prefix + newc 


        # k is decreased, because  
        # we have added a new character 
        printAllKLengthRec(set, newPrefix, n, k - 1) 

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  def recursiveAdd(recursion,handslist=[[]]):
    if recursion == n:
      return handslist
    results = []    
    for singleResult in handslist.copy():
      rockList = singleResult.copy()+ ["rock"]
      paperList = singleResult.copy()+ ["paper"]
      sissorsList = singleResult.copy()+["scissors"]
      results.append(rockList)
      results.append(paperList)
      results.append(sissorsList)
    return recursiveAdd(recursion+1,results)

  return  recursiveAdd(0)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
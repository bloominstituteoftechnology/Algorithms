#!/usr/bin/python

import sys
import random
from collections import deque
def rock_paper_scissors(n):
  stack=[[]]
  list_of_ways= [['rock'],['paper'],['scissors']]

 

  
  if n==0:
     return stack

  if n==1:
     
     return list_of_ways
      
  if n>1:
     y = n*2
     stack.remove(stack[0])
     for i in range(y):
       player_one = random.choice(list_of_ways)
       stack.append(player_one)
       
       player_two = random.choice(list_of_ways)
       stack.append(player_two)
       
  return stack


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
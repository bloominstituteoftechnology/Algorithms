#!/usr/bin/python

import sys

# def rock_paper_scissors(n):
  
#   if n <= 0:
#       return [[]]
#   # elif n == 1: 
#   #     return [['rock'], ['paper'], ['scissors']]
#   else:
#     rps = rock_paper_scissors(n - 1)
#     answer = []
#     for i in rps:
      
#       answer.append(i + ['rock'])
#       answer.append(i + ['paper'])
#       answer.append(i + ['scissors'])
      
#     return answer 

def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  count = 1
  answer = [['rock'], ['paper'], ['scissors']]
  if n == 1:
    return answer
  while count < n:
    answer = recursion_helper(answer)
    count += 1
  return answer

def recursion_helper(list):
  possibilities = [['rock'],['paper'],['scissors']]
  new_list = []
  for item in list:
    for possibility in possibilities:
      new_list.append(item + possibility)
  return new_list

print(rock_paper_scissors(6))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
#!/usr/bin/python

import sys
import math
import itertools

def rock_paper_scissors(n):


  # if n == 0:
  #   return [[]]
  # if n == 1:
  #   return [['rock'], ['paper'], ['scissors']]
  # ret_arr = []
  # obj = {
  #   'rock': [['rock']],
  #   'paper': [['paper']],
  #   'scissors': [['scissors']]
  # }
  # arr = [['rock'], ['paper'], ['scissors']]

  # for key in obj:
  #   for x in range(n):
  #     obj[key] = [[key] for i in range(3**(n-1))]
  # print('OBJ', obj)
  # def inner_keys(o, num, x):
  #   if x < 2: 
  #     return o
  #   i = 0
  #   for key in o:
  #     for el in o[key]:
  #       print(arr[i])
  #       el.extend(arr[i])
  #       if i < 2:
  #         i += 1
  #       else:
  #         i = 0
  #   print('OBJ_inner', o)
  #   x -= 1
  #   return inner_keys(o, n-1, x)
  # inner_keys(obj, n, n)
  # # inner_keys(obj, n)
  #   # i = 0
  #   # j = 0
  #   # for key in obj:
  #   #   for el in obj[key]:
  #   #     # print(j, i)
  #   #     el.extend([arr[j][0], arr[i][0]])
  #   #     if i < 2:
  #   #       i += 1
  #   #     else:
  #   #       i = 0
  #   #       if j < 2:
  #   #         j += 1
  # for k in obj:
  #   ret_arr.extend(obj[k])
  # # print('RET', ret_arr)
  # return ret_arr
print(rock_paper_scissors(3))

  # 
  #
  #
  # 
  # return n


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
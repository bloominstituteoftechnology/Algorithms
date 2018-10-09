#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    items_length = len(items)

    def helper(n, c):
        if n == 0 or c == 0:
            return 0
        elif items[n-1].size > c:
            return helper(n-1, c)
        else:
            return max(helper(n-1, c), items[n-1].value + helper(n-1, c - items[n-1].value))
    return helper(items_length, capacity)


"""
The value/weight ratio implementation is a greedy algorithm, which would work for some cases,
but won't fulfill many edge cases. In this case, a dynamic programming approach with memoization
would be superior to the greedy approach.
"""
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
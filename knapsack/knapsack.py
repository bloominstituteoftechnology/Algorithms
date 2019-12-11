#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  knapsack = []
  curr_capacity = 0
  for i in items:
    if curr_capacity + i.size <= capacity:
      knapsack.append(i)
    elif knapsack[-1].value / knapsack[-1].size > i.value / i.size:
      for j in range(len(knapsack)-2, -1, -1):
        if knapsack[j].value / knapsack[j].size < i.value / i.size:
          s = 0
          for k in knapsack[:j]:
            s += k.capacity
          if
  

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
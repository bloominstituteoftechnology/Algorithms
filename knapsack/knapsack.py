#!/usr/bin/python

import sys
from collections import namedtuple

#The first row number is just a row/observation number, to facilitate reading and referring to items. 
# The second number is the size/cost of the item, i.e. the cost of putting it in your knapsack. 
# The third number is the value, i.e. the utility/payoff you get for selecting that item. 
# The program should also take as input a total size, which can just be a number passed from 
# the command line. So execution may look like this: `python knapsack.py input.txt 100`.

#The goal is to select a subset of the items to maximize the payoff such that the cost 
# is below some threshold. That is, the output should be a set of items (identified by number) 
# that solves the Knapsack problem. It's also worth outputting the total cost and value 
# of these items. This can all just be printed and may look something like below.

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  return items, capacity
  

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
#!/usr/bin/python
# Create an instance of KnapsackSolver.
# Declare the values, weights, and capacities.
# Initialize the solver with that data.
# Call the Solve() method.
# Display the result.

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity, index=0, total_value=0, choices=[]):
  if index>= len(items):
    return [total_value, choices]
  else:
      if items[index].size <= capacity:
        choices_copy = choices.copy()
        choices_copy.append(items[index].index)
        return max(
            knapsack_solver(
              items,
              capacity - items[index].size,
              index +1,
              total_value + items[index].value,
              choices_copy,
        ),
        knapsack_solver(items,capacity, index+1, total_value, choices),
        key=lambda i: i[0],
      )
      else:
        return knapsack_solver(items, capacity, index + 1, total_value, choices)
 
  

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

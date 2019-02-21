#!/usr/bin/python
# some of the time complexity thoughts from c / c++ programming : https://www2.cs.arizona.edu/~mercer/Presentations/12-AlgorithmAnalysis.pdf

# found this stack overflow thread useful when thinking of how to approach the concept of this kanpsack problem : https://stackoverflow.com/questions/6164629/dynamic-programming-and-memoization-bottom-up-vs-top-down-approaches

# looking over bottom-up vs top-down for this problem : https://www.interviewcake.com/concept/java/bottom-up

# also found this article to be of use. it shows the process using fib but it can be applied to the concept of this to solve it : https://medium.com/@andrewsouthard1/dynamic-programming-recursion-memoization-and-bottom-up-algorithms-61c882d1c7e
# testing : Ran 3 tests in 0.279s
import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

# trying to do my first pass of dynamic programming with memorization 
# utilizing a bottom up approach. which is a bit backward to my general way of thinking.
# but lets see how well it works

def knapsack_solver(items, capacity):

  # using a nested list comprehension we can make our initial cache
  cache = [[{} for k in range(capacity + 1)] for k in range(len(items) + 1)]

  # still using a nested for loop so there still may be alot of room for optimization

  # going to iterate over a range of length of items + 1
  for i in range(len(items) + 1):
    # inner look will itterate over a range of capacity + 1
    for j in range(capacity + 1):
      # if we are at the first iteration then set the Value to zero and the Chosen to an empty list
      if i == 0 or j == 0:
        cache[i][j] = {'Value': 0, 'Chosen': []}
      # otherwise if the size of the items list element at i - 1 is greater than j
      # set the cache of [i][j] value to the cache of [i - 1][j] value
      elif items[i - 1].size > j:
        cache[i][j] = cache[i - 1][j]
      # and if both conditions are not met lets set a first case to hold the cache at [i - 1][j] value
      # and the second_case to hold a dictionary with the values from the i - 1 j - items at i - 1.size at the key of Value plus the value of the items at i - 1
      # and the chosen of cache at i - 1 j ath the size of items at i - 1 at the key of Chosen plus the index of the items at i - 1 
      else:
        first_case = cache[i - 1][j]
        second_case = {'Value': cache[i-1][j-items[i-1].size]['Value'] + items[i-1].value, 'Chosen': cache[i-1][j-items[i-1].size]['Chosen'] + [items[i-1].index]}
        # taken out derived dynamic case test if the first case at the key of value is greater than the second case at the key of value
        # set the cache at [i][j] to the first case. Otherwise set cache at [i][j] to the second case
        if first_case['Value'] > second_case['Value']:
          cache[i][j] = first_case
        else:
          cache[i][j] = second_case
  # finally return the cache at the derived [length of items][capacity]
  return cache[len(items)][capacity]
  

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
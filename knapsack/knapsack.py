import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

"""
Brute-force knapsack checks every possible combination of items we could 
be taking and outputs the combination with the best value. 
1. Use recursion to exhaustively check every single combination of items
2. Base case 1: we have no items left in the pile to take
3. Base case 2: we have one item left in the pile. Check to see if it fits. If it does, take it, otherwise discard it.
4. On each recursive call we pick up the next item from the pile
5. Calculate the overall value we have in our knapsack if we don't take the item
6. Calculate the overall value we have in our knapsack if we do take the item
7. Compare the two calculated values; take the option that yields the greater value
"""

# def knapsack_solver(items, capacity):
#   # Recursively check all combinations of items with inner helper method
#   def knapsack_rec(items, capacity, value=0, bag=set()):
#     # No remaining items that fit
#     if not items:
#       return value, bag
#     elif items[0].size > capacity:
#         return knapsack_rec(items[1:], capacity, value, bag)
#     else:
#       # Recurse cases of taking item/not taking item, return max
#       bag_copy = bag.copy() # Copy to avoid marking everything taken
#       bag_copy.add(items[0].index)
#       # Calculate the value of taking this item
#       r1 = knapsack_rec(items[1:], capacity - items[0].size,
#                         value + items[0].value, bag_copy)
#       # Calculate the value of not taking this item
#       r2 = knapsack_rec(items[1:], capacity, value, bag)
#       # Choose the option with the larger value
#       return max(r1, r2, key=lambda tup: tup[0])
#   # Initial call with our bag represented as a Set data structure
#   answer = knapsack_rec(items, capacity)
#   return {'Value': answer[0], 'Chosen': sorted(list(answer[1]))}



# Memoized version of our brute-force solution
def knapsack_solver(items, capacity):
  cache = [[0] * (capacity + 1) for _ in range(len(items) + 1)]

  def knapsack_memoized_helper(index, capacity, value=0, bag=set()):
    answer = cache[index][capacity]
    if answer == 0:
      answer = knapsack_bf_helper(index, capacity, value, bag)
      cache[index][capacity] = answer
    return answer

  def knapsack_bf_helper(index, capacity, value=0, bag=set()):
    # No remaining items that fit
    if index == -1:
      return value, bag
    elif items[index].size > capacity:
        return knapsack_memoized_helper(index - 1, capacity, value, bag)
    else:
      # Recurse cases of taking item/not taking item, return max
      bag_copy = bag.copy() # Copy to avoid marking everything taken
      bag_copy.add(index)
      # Calculate the value of taking this item
      r1 = knapsack_memoized_helper(index - 1, capacity - items[index].size, value + items[index].value, bag_copy)
      # Calculate the value of not taking this item
      r2 = knapsack_memoized_helper(index - 1, capacity, value, bag)
      # Choose the option with the larger value
      return max(r1, r2, key=lambda tup: tup[0])
    
  answer = knapsack_bf_helper(len(items) - 1, capacity)
  return {'Value': answer[0], 'Chosen': sorted(list(answer[1]))}


"""
Incorrect but feasible and efficient solution for the knapsack problem.
"""
# def knapsack_solver(items, capacity):
#   value = 0
#   weight = 0
#   bag = set() 
#   # Relax the problem by considering items in increasing order of weight by value
#   norm_items = [Item(item.index, float(item.size) / item.value, item.value) for item in items]
#   sorted_items = sorted(norm_items, key=lambda item: item.size)

#   # Greedy loop, if the item fits in the knapsack, take it
#   for item in sorted_items:
#     if weight + (item.size * item.value) <= capacity:
#       bag.add(item.index)
#       value += item.value
#       weight += (item.size * item.value)

#   return {'Value': value, 'Chosen': sorted(list(bag))}


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
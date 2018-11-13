#!/usr/bin/python

import sys

def climbing_stairs(n, cache = {}):
  
  if n <= 1:
  	return 1
  if n == 2:
  	return 2

  if n not in cache:
  	cache[n] = climbing_stairs(n-1, cache) + climbing_stairs(n-2, cache) + climbing_stairs(n-3, cache)
  
  return cache[n]


# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_stairs = int(sys.argv[1])
#     print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
#   else:
#     print('Usage: climbing_stairs.py [num_stairs]')
print(climbing_stairs(50, {}) == 10562230626642)
print(climbing_stairs(100, {}) == 180396380815100901214157639)
print(climbing_stairs(500, {}) == 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527)

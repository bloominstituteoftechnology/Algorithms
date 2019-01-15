#!/usr/bin/python

import sys

def making_change(amount, denominations, cache=None):
  
  if amount <= 0 or len(denominations) == 0:
    return 1
  
  # Set up a cache
  local_cache = cache
  if local_cache == None:
    local_cache = {}
    
  # Turn the denominations list into a string so it can be used as a key
  denominations_key = ", ".join(str(x) for x in denominations)
  
  # Check if we have a cache for a given list of denominations yet, or make a new one
  if local_cache.get(denominations_key, None) == None:
    local_cache[denominations_key] = {}
  
  # Check if we have a result for this amount of coins already, given the current denominations
  if local_cache[denominations_key].get(amount, None) != None:
    return local_cache[denominations_key][amount]
  
  number_of_possibilities = 0
  
  for denomination in denominations:
    max_number_denomination = amount // denomination
    
    if max_number_denomination == 0:
      continue  # go to next denomination
      
    new_denominations = []
    # make a new denomination list with only denominations smaller than the one we are inspecting
    for old_denomination in denominations:
      if old_denomination < denomination:
        new_denominations.append(old_denomination)
        
    # If there are no denominations to check, continue
    if len(new_denominations) == 0:
      number_of_possibilities += 1
      continue
      
    for number_of_denominations in range(1, max_number_denomination + 1):
      remainder = amount - (number_of_denominations * denomination)
      
      if remainder == 0:
        number_of_possibilities += 1
      else:
        number_of_possibilities += making_change(remainder, new_denominations, cache=local_cache)
  
  # Save results to the cache
  local_cache[denominations_key][amount] = number_of_possibilities
  return number_of_possibilities
  

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
#!/usr/bin/python

import sys


def making_change(amount, denominations):
  if amount <= 4:
      return 1
  def helper_method(hm_amount, hm_denoms):

    # Find the highest denomination in hm_denomination list that is less or equal to hm_amount
    def max_denom(md_amount, md_denoms):
      max_denom = 0
      for i in md_denoms:
        if i > max_denom and i <= md_amount:
          max_denom = i
      return max_denom
    
    reversed_denoms = list(reversed(hm_denoms))
    max_denom = max_denom(hm_amount, hm_denoms)
    # Iterate through the reversed denomination list, from the highest denom just less of max_denom, to 5
    for j in reversed_denoms[reversed_denoms.index(max_denom):-1]:
      max_quotient = int(hm_amount // max_denom)
      for k in range(1,max_quotient):

        counter = (hm_amount // max_denom) + helper_method(hm_amount - k*max_denom, hm_denoms) - 1
    return counter + 1

  return helper_method(amount, denominations) 

  #   for i in hm_denominations 



  #   elif amount >= 5 and amount < 10:
  #     return 2
  #   elif amount >= 10 and amount < 15:
  #     return 3
  #   elif amount >= 15 and amount < 20:




  # # for i in denominations:
  # reversed_list =denominations[::-1]
  # print(reversed_list[0:-1])
  
  # def helper_method(counter, hm_amount, hm_denominations):
  #   for value in hm_denominations:
  #     print(value)
  #     # if value == hm_denominations[len(hm_denominations)-1]:
  #     #   print('endpoint: ' + str(hm_amount//value))
  #     #   return hm_amount//value
  #     if value <= hm_amount:
  #       print('here')
        
  #       counter = hm_amount//value + helper_method(counter, hm_amount % value, hm_denominations)
  #   print("counter: " + str(counter))
  #   return counter

  # return  helper_method(0, amount, reversed_list[0:-1]) + 1

denominations = [1, 5, 10, 25, 50]
print('final: ' + str(making_change(15, denominations)))

  # if amount < 5:
  #   count = 1
  # elif amount >= 5 and amount < 10:
  #   count = 2
  # elif amount >=10 and amount < 15:
  #   count = 4
  # elif amount >=15 and amount < 20:
  # else:
  #   count = count + climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
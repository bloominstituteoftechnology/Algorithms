#!/usr/bin/python

import sys

denominations = {
  'penny': 1,
  'nickel': 5,
  'dime': 10,
  'quarter': 25,
  'half_dollar': 50
}

def making_change(amount, denominations):
  amount_as_string = str(amount)
  ones_place = int(amount_as_string[1])
  tens_place = int(amount_as_string[0])
  ways = 0
  if amount <= 0:
    return 0
  elif amount in range(1,5):
    ways += 1
    return ways
  elif amount == 5:
    ways += 2
    return ways
  elif len(str(amount)) == 1:
    return
  elif len(str(amount)) == 2:
    if ones_place == 0:
      ways += 0
      if tens_place == 1:
        ways += 4
        return ways
    elif ones_place == 2:
      ways += 8
      if ones_place == 0:
        return ways
      elif ones_place in range(1,5):
        ways += 4
        return ways
      

      # ways += 1
      # if tens_place == 1:
      #   ways += 4
      # elif tens_place == 2:
      #   ways += 8
      #   return ways
    
print(making_change(20, denominations))  
    
    # else:
    # ways += 8
    # return ways



  #   return 1
  # elif amount in range(5,:
  #   return 1  
  # else: 
  #   return 7

 


# def climbing_stairs(n):
#   #base case
#   if n < 0:
#     return 0 
#   elif n == 0 or n == 1:
#     return 1
#   elif n == 2:
#     return 2
#   elif n == 3:
#     return 4
#   #move towards one of our base cases
#   return climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)

# print(climbing_stairs(10))





if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  combinations = 0

  if n == 0:
    return 1

  def fact(num):
    if num < 1:
      factorial = 0
    else:
      factorial = 1
      while num >= 1:
        factorial *= num
        num -= 1
    return factorial
  
  # print('factorial check:', fact(3))

  nums = [1, 2, 3]

  
  # how many ways can you make combos with one number
  for i in nums:
    # print(f'starting {i}')
    if (n / i) >= 1 and n % i == 0:
      # print(f'1 number: {i}')
      combinations += 1

  print('combinations for 1:', combinations)

  # how many ways can you make combos with 2 numbers
  two_num_combos = []
  for i in nums:
    for j in nums:
      if i != j:
        if i + j <= n:
          if [j,i] not in two_num_combos:
            two_num_combos.append([i,j])

  print('two num combos',two_num_combos)
  print('solving equation for 2 num')

  for i in two_num_combos:
    # xi[0] + yi[1] = n
    # solve the equation
    y = 1
    x_range = n // i[0] + 1
    y_range = n // i[1] + 1

    print('x range', x_range)
    print('y range', y_range)
    

    for x in range(1, x_range):
      for y in range(1, y_range):
        if x*i[0] + y*i[1] == n:
          print(x * [i[0]], y * [i[1]])
          print(f'x:{x}, y:{y}')
          combinations += fact(x+y)// (fact(x)*fact(y))

          print('fact',fact(x+y)//2)


  # how many ways can you make combos with 3 numbers
  three_num_combos = []
  
  if sum(nums) <= n:
    three_num_combos.append(nums)

  for i in three_num_combos:
    # xi[0] + yi[1] + zi[2] = n
    # solve the equation

    x_range = n // i[0] + 1
    y_range = n // i[1] + 1
    z_range = n // i[2] + 1

    print('x range', x_range)
    print('y range', y_range)
    print('z range', z_range)
    

    for x in range(1, x_range):
      for y in range(1, y_range):
        for z in range(1, z_range):
          if x*i[0] + y*i[1] + z*i[2]== n:
            print(x * [i[0]], y * [i[1]], z * [i[2]])
            print(f'x:{x}, y:{y}, z:{z}')
            combinations += fact(x+y+z)// (fact(x)*fact(y)*fact(z))


  return combinations

print(eating_cookies(0))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')
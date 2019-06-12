#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

[1]
[1,1]
[2]
[3]
[1,1,1]
[2,1]

def factorial(n):
	num = 2
	total = 1
	while num <= n:
		total = total * num
		num+=1

	return total



def repeat_permutation(arr):
	unique = list(set(arr))
	possibilities = factorial(len(arr))
	for item in unique:
		possibilities = possibilities // factorial(arr.count(item))
	return int(possibilities)

# repeat_permutation([6,6,6,4,4,4,3,3,6])



	

def eating_cookies(n, cache=None):
	cookies = n
	total = 0
	total_ways = []
	way = []
	if n == 0:
		return 1
	for i in range(0,n+1):
		for j in range(0, (n//2)+ 1):
			for k in range(0, (n//3)+ 1):
				if i + 2*j + 3*k == n:
					# print(f'A solution is ({i}, {j}, {k})')
					way = ([1]*i) + ([2]*j) + ([3]*k)
					# print(way)
					if len(way) != 0: 
						total_ways.append(way)
						
		way=[]



	for Rrr in total_ways:
		total = total + repeat_permutation(Rrr)
	
	return total

	# while cookies > 0:
	# 	way.append(1)
	# 	cookies = cookies - 1
	# total_ways.append(way)
	# way = [way[i] + way[i+1] in way if i+1 [1:2] = [way[1] + way[2]]
	# print(way)

	# cookies = n
	# if cookies%2 != 0:
	# 	way.append(1)
	# 	cookies = cookies - 1
	# 	while cookies > 0:
	# 		way.append(2)
	# 		cookies = cookies - 2
	# total_ways.append(way)
	# print(total_ways)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
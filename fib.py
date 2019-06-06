"""
Fibonacci sequence

Write a function that computes the nth Fibonacci number.

n is a non-negative integer.

0  1  2  3  4  5  6  7   8   9   10
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
"""

import sys

sys.setrecursionlimit(40010)

def fib(n):
	cache = {}   # Memoization

	def fib_inner(n): # O(n)
		nonlocal cache

		# TODO make sure n is non-negative

		if n == 0:
			return 0

		if n == 1:
			return 1

		if n not in cache:
			cache[n] = fib_inner(n-1) + fib_inner(n-2)

		return cache[n]

	return fib_inner(n)

for i in range(20000,40000): # start at 30K for segfault
	print(f'{i}: {fib(i)}')


++++++++++++++++++++++++++

def fib_bottom_up(n):
	if n == 0:
		return 0

	if n == 1:
		return 1

	pprev = 0
	prev = 1

	i = 1
	while i < n:
		pprev, prev = prev, prev + pprev
		i += 1

	return prev

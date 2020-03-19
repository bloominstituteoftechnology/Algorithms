#!/usr/bin/env python


import sys

from typing import Hashable, Any


class Memoizer:
	'''
	Class to facilitate memoization of function returns.

	Attributes:
		functions (
			Dict[
				callable: Dict[
					Tuple[frozenset, frozenset]: Object
				]
			]
		)
		A dictionary of functions: dictionary of args: results

	Methods:
		get_result: Gets the result of a function call, either
			by returning the stored result or by running the
			function if no stored results are found.
	'''

	def __init__(self):
		'''
		Inits a new Memoizer.
		'''

		self.functions = {}

	def get_result(self, function: callable, *args, **kwargs) -> Any:
		'''
		Gets the result of a function call with specific arguments.
		If the function has been called through get_result before with these
			parameters in this Memoizer, this will return the memoized result.
		Otherwise, it will run the function and memoize the new result.

		Args:
			function (callable): The function to run.
				This should *always* be idempotent or nullipotent.
			*args: Variable length argument list. Passed to function.
			**kwargs: Arbitrary keyword arguments. Passed to function.

		Returns:
			Object: The return value of function.
		'''

		if function not in self.functions:
			self.functions[function] = {}

		params = (frozenset(args), frozenset(kwargs))

		if params in self.functions[function]:
			return self.functions[function][params]
		else:
			self.functions[function][params] = function(*args, **kwargs)
			return self.functions[function][params]


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies_recursive(n, cache=None):
	if n < 0:
		return 0
	elif n == 0:
		return 1

	if cache is None:
		cache = Memoizer()
		for i in range(n):
			cache.get_result(
				eating_cookies_recursive,
				i,
				cache=cache
			)

	permutations = 0
	can_eat = [1, 2, 3]
	for cookie_count in can_eat:
		permutations += cache.get_result(
			eating_cookies_recursive,
			n - cookie_count,
			cache=cache
		)

	return permutations


eating_cookies = eating_cookies_recursive


if __name__ == "__main__":
	if len(sys.argv) > 1:
		num_cookies = int(sys.argv[1])
		print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
	else:
		print('Usage: eating_cookies.py [num_cookies]')



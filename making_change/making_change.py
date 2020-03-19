#!/usr/bin/env python

import sys

from typing import Hashable, Any, Iterable


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

		params = (self.make_hashable(args), self.make_hashable(kwargs))

		if params in self.functions[function]:
			return self.functions[function][params]
		else:
			self.functions[function][params] = function(*args, **kwargs)
			return self.functions[function][params]

	@staticmethod
	def make_hashable(obj) -> Hashable:
		try:
			hash(obj)  # Isinstance Hashable fails on nested objects
			return obj
		except TypeError:
			if isinstance(obj, dict):
				return tuple(sorted((Memoizer.make_hashable((key, value)) for key, value in obj.items())))
			elif isinstance(obj, Iterable):
				return tuple((Memoizer.make_hashable(value) for value in obj))
			try:
				return frozenset(obj)
			except TypeError:
				result = []
				for item in obj:
					result.append(make_hashable(item))
				return tuple(result)


def making_change(amount, denominations, cache=None):
	if amount < 0:
		return 0
	elif amount == 0:
		return 1

	if not isinstance(denominations, tuple):
		# This is faster than using make_hashable
		denominations = tuple(denominations)

	if cache is None:
		cache = Memoizer()

		# Fill the cache from simple cases to complex
		# to avoid recursion limits
		for i in range(amount):
			cache.get_result(
				making_change,
				i,
				denominations,
				cache=cache,
			)

	combinations = 0
	inversed_denominations = cache.get_result(
		inverse_sort,
		denominations,
	)
	for i, denomination in enumerate(inversed_denominations):
		combinations += cache.get_result(
			making_change,
			amount - denomination,
			inversed_denominations[i:],
			cache=cache
		)

	return combinations


def inverse_sort(tup):
	return tuple(sorted(tup, reverse=True))


if __name__ == "__main__":
	# Test our your implementation from the command line
	# with `python making_change.py [amount]` with different amounts
	if len(sys.argv) > 1:
		denominations = [1, 5, 10, 25, 50]
		amount = int(sys.argv[1])
		print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
	else:
		print("Usage: making_change.py [amount]")
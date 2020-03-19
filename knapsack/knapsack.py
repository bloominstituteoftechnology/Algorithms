#!/usr/bin/env python

import sys

from collections import namedtuple
from pprint import pprint
from typing import Iterable, Hashable, Any

Item = namedtuple('Item', ['index', 'size', 'value'])


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

	def get_result(self, function: callable, *args, assume_hashable_args=True, **kwargs) -> Any:
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

		if assume_hashable_args:
			params = (tuple(args), self.make_hashable(kwargs))
		else:
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
			return json.dumps(obj)


def knapsack_inner(items, capacity, cache=None):
	if cache is None:
		cache = Memoizer()
		for lower_capacity in range(0, capacity, 10):
			print(lower_capacity)
			cache.get_result(
				knapsack_inner, items, lower_capacity, cache=cache, assume_hashable_args=False
			)

	options = {}
	for item in items:
		if item.size > capacity:
			continue

		new_items = items[:]
		new_items.remove(item)
		new_capacity = capacity - item.size

		result = cache.get_result(
			knapsack_inner, new_items, new_capacity, cache=cache, assume_hashable_args=False
		)

		options[item] = {
			'value': item.value + result['value'],
			'weight': item.size + result['weight'],
			'best_option': result['best_option'],
		}

	best_option = {'value': 0, 'weight': 0}
	best_item = None
	for item, option in options.items():
		if option['value'] > best_option['value']:
			best_option = option
			best_item = item

	retval = {
		'value': best_option['value'],
		'weight': best_option['weight'],
		'best_option': {best_item: best_option}
	}

	return retval


def knapsack_solver(items, capacity):
	results = knapsack_inner(items, capacity)
	items = []
	current_item = results
	while None not in current_item['best_option']:
		item = list(current_item['best_option'].keys())[0]
		items.append(item)
		current_item = current_item['best_option'][item]

	retval = {
		'Value': results['value'],
		'Chosen': [item.index for item in items]
	}
	return retval


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
		pprint(knapsack_solver(items, capacity))
	else:
		print('Usage: knapsack.py [filename] [capacity]')

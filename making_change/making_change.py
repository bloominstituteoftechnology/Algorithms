#!/usr/bin/env python

import sys

from typing import Hashable, Any, Iterable


def make_hashable(obj) -> Hashable:
	try:
		hash(obj)  # Isinstance Hashable fails on nested objects
		return obj
	except TypeError:
		if isinstance(obj, dict):
			return tuple(sorted((make_hashable((key, value)) for key, value in obj.items())))
		elif isinstance(obj, Iterable):
			return tuple((make_hashable(value) for value in obj))
		try:
			return frozenset(obj)
		except TypeError:
			result = []
			for item in obj:
				result.append(make_hashable(item))
			return tuple(result)


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def making_change(n, denominations, denomination_counts=None, parent_denominations=None):
	if n < 0:
		return 0
	elif n == 0:
		return 1

	if denomination_counts is None:
		denomination_counts = set()
	if parent_denominations is None:
		parent_denominations = {
			denomination: 0 for denomination in denominations
		}

	# print(denomination_counts)

	combinations = 0
	for denomination in denominations:
		new_denominations = parent_denominations.copy()
		new_denominations[denomination] += 1
		if make_hashable(new_denominations) not in denomination_counts:
			if n - denomination >= 0:
				denomination_counts.add(make_hashable(new_denominations))
				combinations += making_change(
					n - denomination,
					denominations,
					denomination_counts=denomination_counts,
					parent_denominations=new_denominations,
				)

	return combinations


if __name__ == "__main__":
	# Test our your implementation from the command line
	# with `python making_change.py [amount]` with different amounts
	if len(sys.argv) > 1:
		denominations = [1, 5, 10, 25, 50]
		amount = int(sys.argv[1])
		print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
	else:
		print("Usage: making_change.py [amount]")
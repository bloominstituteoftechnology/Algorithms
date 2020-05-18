import unittest
import random
from product_of_all_other_numbers import product_of_all_other_numbers

class Test(unittest.TestCase):
    def test_product_of_all_other_numbers(self):
        self.assertEqual(product_of_all_other_numbers([9, 90]), [90, 9])
        self.assertEqual(product_of_all_other_numbers([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])

        arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]
        expected = [13547520, 10536960, 94832640, 11854080, 15805440, 13547520, 11854080, 11854080, 13547520, 9483264]

        self.assertEqual(product_of_all_other_numbers(arr), expected)

        arr = [7, 9, 1, 8, 6, 0, 7, 8, 8, 7, 10]
        expected = [0, 0, 0, 0, 0, 94832640, 0, 0, 0, 0, 0]

        self.assertEqual(product_of_all_other_numbers(arr), expected)


if __name__ == '__main__':
    unittest.main()
import unittest
from climbing_stairs import climbing_stairs

class Test(unittest.TestCase):

  def test_climbing_stairs_small_n(self):
    self.assertEqual(climbing_stairs(0), 1)
    self.assertEqual(climbing_stairs(1), 1)
    self.assertEqual(climbing_stairs(2), 2)
    self.assertEqual(climbing_stairs(5), 13)
    self.assertEqual(climbing_stairs(10), 274)

  def test_climbing_stairs_large_n(self):
    self.assertEqual(climbing_stairs(50, [0 for i in range(51)]), 10562230626642)
    self.assertEqual(climbing_stairs(100, [0 for i in range(101)]), 180396380815100901214157639)
    self.assertEqual(climbing_stairs(500, [0 for i in range(501)]), 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527)


if __name__ == '__main__':
  unittest.main()

  
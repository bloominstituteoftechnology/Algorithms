import unittest
from counting_stairs import counting_stairs

class Test(unittest.TestCase):

  def test_counting_stairs_small_n(self):
    self.assertEqual(counting_stairs(0), 1)
    self.assertEqual(counting_stairs(1), 1)
    self.assertEqual(counting_stairs(2), 2)
    self.assertEqual(counting_stairs(5), 13)
    self.assertEqual(counting_stairs(10), 274)

  def test_counting_stairs_large_n(self):
    self.assertEqual(counting_stairs(50, [0 for i in range(51)]), 10562230626642)
    self.assertEqual(counting_stairs(100, [0 for i in range(101)]), 180396380815100901214157639)
    self.assertEqual(counting_stairs(500, [0 for i in range(501)]), 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527)

if __name__ == '__main__':
  unittest.main()

  
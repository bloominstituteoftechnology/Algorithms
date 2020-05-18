import unittest
from sliding_window_max import sliding_window_max

class Test(unittest.TestCase):
    def test_sliding_window_max_1(self):
        arr = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        output = sliding_window_max(arr, k)
        expected = [3, 3, 5, 5, 6, 7]

        self.assertEqual(output, expected)

    def test_sliding_window_max_2(self):
        arr = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 2  
        output = sliding_window_max(arr, k)
        expected = [3, 3, -1, 5, 5, 6, 7]

        self.assertEqual(output, expected)

    def test_sliding_window_max_3(self):
        arr = [70, 37, 100, 66, 1, 45, 27, 62, 75, 57, 92, 66, 9, 39, 15, 69, 46, 72, 35, 68, 54, 51, 35, 36, 13, 27, 27, 24, 6, 33, 83, 97, 55, 5, 25, 85, 56, 4, 100, 38, 38, 83, 29, 1, 11, 27, 64, 99, 64, 29, 41, 95, 59, 46, 75, 67, 40, 49, 62, 30, 56, 88, 71, 77, 43, 79, 27, 65, 24, 18, 74, 50, 23, 47, 45, 60, 62, 84, 53, 2, 90, 29, 99, 75, 59, 44, 71, 7, 59, 59, 27, 72, 6, 89, 90, 40, 51, 45, 43, 86]
        k = 5
        output = sliding_window_max(arr, k)
        expected = [100, 100, 100, 66, 75, 75, 92, 92, 92, 92, 92, 69, 69, 72, 72, 72, 72, 72, 68, 68, 54, 51, 36, 36, 27, 33, 83, 97, 97, 97, 97, 97, 85, 85, 100, 100, 100, 100, 100, 83, 83, 83, 64, 99, 99, 99, 99, 99, 95, 95, 95, 95, 75, 75, 75, 67, 62, 88, 88, 88, 88, 88, 79, 79, 79, 79, 74, 74, 74, 74, 74, 60, 62, 84, 84, 84, 90, 90, 99, 99, 99, 99, 99, 75, 71, 71, 71, 72, 72, 89, 90, 90, 90, 90, 90, 86]

        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
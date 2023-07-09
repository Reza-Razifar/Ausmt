import unittest
from main_981608135 import sum_numbers
class TestSumNumbers(unittest.TestCase):
    
    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(2, 3), 5)
        self.assertEqual(sum_numbers(-2, 2), 0)
        self.assertEqual(sum_numbers(0, 5), 5)
        self.assertEqual(sum_numbers(-100, 100), 0)
        self.assertEqual(sum_numbers(10, 10), 20)

if __name__ == "__main__":
    unittest.main()
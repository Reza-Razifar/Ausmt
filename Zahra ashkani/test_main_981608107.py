import unittest
from main_981608107 import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(3, 4)
        self.assertEqual(result, 7)

    def test_add_negative_numbers(self):
        result = add_numbers(-5, -2)
        self.assertEqual(result, -7)

    def test_add_positive_negative_numbers(self):
        result = add_numbers(8, -3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
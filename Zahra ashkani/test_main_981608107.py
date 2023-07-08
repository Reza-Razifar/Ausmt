import unittest
import main_981608107.py

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(function.add_numbers(2, 3), 5)
        self.assertEqual(function.add_numbers(-2, 3), 1)
        self.assertEqual(function.add_numbers(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
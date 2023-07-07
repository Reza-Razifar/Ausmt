import unittest
from prime import is_prime

class TestPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(10), False)
        self.assertEqual(is_prime(21), False)

if __name__ == '__main__':
    unittest.main()
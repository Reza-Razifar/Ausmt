import unittest
from main import is_prime


class TestIsPrime(unittest.TestCase):
    def test_isPrime(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(6), False)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(8), False)
        self.assertEqual(is_prime(9), False)
        self.assertEqual(is_prime(10), False)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(12), False)
        self.assertEqual(is_prime(13), True)
        self.assertEqual(is_prime(14), False)
        self.assertEqual(is_prime(15), False)
        self.assertEqual(is_prime(16), False)
        self.assertEqual(is_prime(17), True)
        self.assertEqual(is_prime(18), False)
        self.assertEqual(is_prime(19), True)
        self.assertEqual(is_prime(20), False)
        self.assertEqual(is_prime(21), False)
        self.assertEqual(is_prime(22), False)
        self.assertEqual(is_prime(23), True)
        self.assertEqual(is_prime(24), False)
        self.assertEqual(is_prime(25), False)
        self.assertEqual(is_prime(26), False)
        self.assertEqual(is_prime(27), False)
        self.assertEqual(is_prime(28), False)


if __name__ == '__main__':
    unittest.main()
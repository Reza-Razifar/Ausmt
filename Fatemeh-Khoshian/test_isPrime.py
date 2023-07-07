import unittest
from isPrime import is_prime as isPrime

class TestIsPrime(unittest.TestCase):

    def test_isPrime(self):
        self.assertEqual(isPrime(2), True)
        self.assertEqual(isPrime(3), True)
        self.assertEqual(isPrime(4), False)
        self.assertEqual(isPrime(5), True)
        self.assertEqual(isPrime(6), False)
        self.assertEqual(isPrime(7), True)
        self.assertEqual(isPrime(8), False)
        self.assertEqual(isPrime(9), False)
        self.assertEqual(isPrime(10), False)
        self.assertEqual(isPrime(11), True)
        self.assertEqual(isPrime(12), False)
        self.assertEqual(isPrime(13), True)
        self.assertEqual(isPrime(14), False)
        self.assertEqual(isPrime(15), False)
        self.assertEqual(isPrime(16), False)
        self.assertEqual(isPrime(17), True)
        self.assertEqual(isPrime(18), False)
        self.assertEqual(isPrime(19), True)
        self.assertEqual(isPrime(20), False)
        self.assertEqual(isPrime(21), False)
        self.assertEqual(isPrime(22), False)
        self.assertEqual(isPrime(23), True)
        self.assertEqual(isPrime(24), False)
        self.assertEqual(isPrime(25), False)
        self.assertEqual(isPrime(26), False)
        self.assertEqual(isPrime(27), False)
        self.assertEqual(isPrime(28), False)
        self.assertEqual(isPrime(29), True)
        self.assertEqual(isPrime(30), False)
        
if __name__ == '__main__':
    unittest.main()

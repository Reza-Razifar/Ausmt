import unittest

def is_prime(num):
    # If the number is less than 2, it is not prime
    if num < 2:
        return False
    
    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True

class PrimeNumberTestCase(unittest.TestCase):
    def test_prime_number(self):
        # Test a prime number
        self.assertTrue(is_prime(23))
    
    def test_non_prime_number(self):
        # Test a non-prime number
        self.assertFalse(is_prime(10))
    
    def test_negative_number(self):
        # Test a negative number
        self.assertFalse(is_prime(-5))
    
    def test_zero(self):
        # Test zero
        self.assertFalse(is_prime(0))
    
    def test_one(self):
        # Test one
        self.assertFalse(is_prime(1))

if __name__ == '__main__':
    unittest.main()

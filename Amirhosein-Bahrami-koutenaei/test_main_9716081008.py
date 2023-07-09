from main import add_numbers
import unittest


class AddNumbersTestCase(unittest.TestCase):
    def test_add_numbers(self):
        # Test case 1: Valid integer inputs
        number1 = 5
        number2 = 3
        expected_result = 8
        actual_result = add_numbers(number1, number2)
        self.assertEqual(actual_result, expected_result)
    def test_float_inputs(self):
        # Test case 2: Valid float inputs
        number3 = 2.5
        number4 = 1.5
        expected_result = 4.0
        actual_result = add_numbers(number3, number4)
        self.assertEqual(actual_result, expected_result)

    def test_negative_inputs(self):
        # Test case 3: Negative inputs
        number5 = -10
        number6 = 5
        expected_result = -5
        actual_result = add_numbers(number5, number6)
        self.assertEqual(actual_result, expected_result)

    def test_zero_inputs(self):
        # Test case 4: Zero inputs
        number7 = 0
        number8 = 0
        expected_result = 0
        actual_result = add_numbers(number7, number8)
        self.assertEqual(actual_result, expected_result)

    def test_string_inputs(self):
        # Test case 5: String inputs
        string1 = "5"
        string2 = "3"
        with self.assertRaises(ValueError):
            add_numbers(string1, string2)

if __name__ == '__main__':
    unittest.main()
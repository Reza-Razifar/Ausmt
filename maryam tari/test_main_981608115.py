# Unit test for main_981608115.py

# name : maryam tari
# student_number :981608115
# email :maryamtari15@gmail.com

from main_981608115 import sum, minus, multiple, division

# test output value
def test_output_sum():
    check = sum(5, 2)
    assert check == 7

def test_output_multiple():
    check = multiple(3, 4)
    assert check == 12

def test_output_division():
    check = division(6, 2)
    assert check == 3

# test output type
def test_type_sum():
    check = type(sum(1, 2))
    assert check == type(0)


def test_type_multiple():
    check = type(multiple(1, 2))
    assert check == type(0)

def test_type_division():
    check = type(division(1, 2))
    assert check == type(0.0)


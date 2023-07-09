# Unit test for app.py

# Name : Parvin Akbari
# Student Number : 991608106
# Email : radparinaz903@gmail.com

from main_991608106 import sum, minus, multiple, division

# test output value
def test_output_sum():
    check = sum(1, 2)
    assert check == 3

def test_output_minus():
    check = minus(5, 2)
    assert check == 3

def test_output_multiple():
    check = multiple(2, 2)
    assert check == 4

def test_output_division():
    check = division(4, 2)
    assert check == 2

# test output type
def test_type_sum():
    check = type(sum(1, 2))
    assert check == type(0)

def test_type_minus():
    check = type(minus(1, 2))
    assert check == type(0)

def test_type_multiple():
    check = type(multiple(1, 2))
    assert check == type(0)

def test_type_division():
    check = type(division(1, 2))
    assert check == type(0.0)


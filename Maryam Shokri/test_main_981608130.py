# Unit test for app.py

# Name :Maryam Shokri
# ID :981608130
# Email :maryam12shokri@gmail.com

from main_981608130 import sum, division

# test value of output
def test_output_sum():
    check = sum(1, )
    assert check == 5


def test_output_division():
    check = division(9, 3)
    assert check == 3

# test type of output
def test_type_sum():
    check = type(sum(1, 2))
    assert check == type(0)


def test_type_division():
    check = type(division(1, 2))
    assert check == type(0.0)


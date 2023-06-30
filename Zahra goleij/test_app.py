# Unit test for app.py

# name :ZahraGoleij
# student_number :981608140
# email :zahragoleij0@gmail.com

from app import sum, multiple

# test output value
def test_output_sum():
    check = sum(1, 2)
    assert check == 3

def test_output_multiple():
    check = multiple(2, 2)
    assert check == 4

# test output type
def test_type_sum():
    check = type(sum(1, 2))
    assert check == type(0)

def test_type_multiple():
    check = type(multiple(1, 2))
    assert check == type(0)


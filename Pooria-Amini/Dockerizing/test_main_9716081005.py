import pytest
from main_9716081005 import is_prime, NotPositive, NotInteger


def test_even_numbers():
    assert not is_prime(10)  # is_prime(10) == False
    assert not is_prime(48750)
    assert is_prime(788888) == False
    assert is_prime(2)  # is_prime(2) == True


def test_non_positive_numbers():
    with pytest.raises(NotPositive):
        is_prime(-50)
    with pytest.raises(NotPositive):
        is_prime(-1)
    with pytest.raises(NotPositive):
        is_prime(0)


def test_some_numbers():
    assert is_prime(139) == True
    assert is_prime(313) == True
    assert is_prime(579) == False  # 3 * 193
    assert is_prime(277) == True


def test_non_integers():
    with pytest.raises(NotInteger):
        is_prime(12.587)
    with pytest.raises(NotInteger):
        is_prime(5.98)

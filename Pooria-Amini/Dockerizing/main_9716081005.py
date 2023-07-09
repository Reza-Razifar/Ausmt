import math


class NotPositive(ValueError):
    def __init__(self, message):
        super().__init__(message)


def is_prime(num):
    if num <= 0:
        raise NotPositive(
            'Entered number can not be a negative or zero number.')
    root = math.sqrt(num)

    for i in range(2, math.floor(root)):
        if num % i == 0:
            return False

    return True

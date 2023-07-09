def add_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Inputs must be numeric.")
    sum = a + b
    return sum
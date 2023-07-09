#Moein_Atiabi 

def is_prime(num):
    # If the number is less than 2, it is not prime
    if num < 2:
        return False
    
    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True

# Test the function
number = 23
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
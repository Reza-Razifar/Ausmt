num_str=input("input your number : ")
num=int(num_str)
def is_prime(num):
    if num < 2:
        return 0
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    
    return 1
print(is_prime(num))
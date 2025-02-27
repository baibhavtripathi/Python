import math

n = int(input('Enter a number to check if it\'s armstrong: '))

def is_armstrong(n) -> bool:
    digits_sum = 0
    no_of_digits = len(str(n))
    temp = n
    while n > 0:
        digits_sum += math.pow(n%10, no_of_digits)
        n //= 10
    return temp == digits_sum

print(is_armstrong(n))
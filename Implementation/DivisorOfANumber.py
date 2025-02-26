n = int(input('Enter a number: '))
divisors = [1]
for i in range(2, n):
    if n % i == 0:
        divisors.append(i)
divisors.append(n)
print('Divisor of {} is {}'.format(n, divisors))

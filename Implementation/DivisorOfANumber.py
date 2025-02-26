class findDivisor:
    divisors = [1]
    def divisorsFun(self, n):
        for i in range(2, n):
            if n % i == 0:
                self.divisors.append(i)
        self.divisors.append(n)
        return self.divisors

if __name__ == '__main__':
    n = int(input('Enter a number: '))
    findDivisor = findDivisor()
    divisorsList = findDivisor.divisorsFun(n)
    print('Divisor of {} is {}'.format(n, divisorsList))
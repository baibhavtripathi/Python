import math
n = int(input('Enter a number to count the digits: '))

# Solution - 1
'''
temp, counter = n, 0

while(temp != 0):
    counter = counter + 1
    temp =  temp // 10

print('Number of digits in {0}: {1}'.format(n, counter))
'''

# Solution - 2 -> Convert to string & find length
#print('Number of digits in {0}: {1}'.format(n, len(str(n))))

# Solution - 3 -> Use math: 
'''
Assuming the logarithm is in base 10, if you take the log of any number in base 10 
and round it up, you will get the number of digits in that number. The number of 
decimal digits in N would be ⌊log10N⌋+1.
'''
print('Number of digits in {0}: {1}'.format(n, (math.floor(math.log10(n))+1)))
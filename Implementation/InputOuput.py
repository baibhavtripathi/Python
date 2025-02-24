import math

# n = int(input('Enter number of elements in the list : '))
# List = list()
# print("Enter the list elements:")

# for i in range(n):
#     List.append(int(input()))

# print(List)

# --- #
print('Enter the list elements:')
List1 = list(map(int, input().split()))
print('List elements are: ', end = '')
print(List1)
print("striver", "tuf", "India", sep=" & ")
print("Factorial of 5 is: ", end="")
print(math.factorial(5))
print("Gcd of 100 and 24 is: ", end="")
print(math.gcd(100, 24))

'''
print(object(s), sep=’ ‘ ,end = ‘\n’, file = file, flush = flush) 
parameter	Description
object(s) 	Any object, and as many as you like. Will be converted to a string before printed
sep 	(Optional). Specify how to separate the objects, if there is more than one. Default is ‘ ‘.
end	(Optional). Specify what to print at the end. Default is ‘\n’.
file	(Optional). An object with a write method. Default is sys. stdout
flush	(Optional). A Boolean specifies if the output is flushed (True) or buffered (False). Default is False
'''
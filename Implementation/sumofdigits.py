'''
Docstring : fun to find sum of digit of a number
Type : int
'''
NUM = int(input("enter the no. : "))
X = NUM // 1000
X1 = (NUM - X*1000)//100
X2 = (NUM - X*1000-X1*100)//10
X3 = NUM - X*1000-X1*100-X2*10

print("sum of digits is:=", X+X1+X2+X3)
print()

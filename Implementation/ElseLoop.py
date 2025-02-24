count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

while count == 5:
    print('Love')
    count += 1
else:
    print("My Love is gone")

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i, "-")
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        continue
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

for x in [1,2,3]:
    print(x)
else:
    print('Else will execute if break not executed in for loop')
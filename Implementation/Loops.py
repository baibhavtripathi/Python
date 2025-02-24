# Can we use "else" clause for loops?
# Unlike languages like C,CPP.. we can use else for loops. 
# When the loop condition of "for" or "while" statement fails then code part in "else" is executed. 
# If a break statement is executed inside the for loop then the "else" part is skipped. 
# Note that the "else" part is executed even if there is a continue statement.

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
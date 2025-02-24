strs = 'CDCDC'
lent = 2
substr = 'DC'
count  = 0
for i in range(len(strs)):
    if i+lent <= len(strs) and strs[i:i+lent] == substr:
        count += 1
print(count)
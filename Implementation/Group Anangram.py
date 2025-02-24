#Group Anangram
st = 'baibhav'
ch_arr = [0]*26
for i in st:
    ch_arr[ord(i)-ord('a')] += 1
print(str(ch_arr))

def nForest(n:int) ->None:
    for i in range(1, n+1):
        if i%2 != 0:
            # print(str(n-i)*(n-i))
            shift = (n-i)//2
            print(' '*shift + '*'*i + ' '*shift)
    for i in range(1, n+1):
        if i%2 != 0:
            # print(str(n-i)*(n-i))
            shift = (i)//2
            print(' '*shift + '*'*(n+1-i) + ' '*shift)

nForest(9)
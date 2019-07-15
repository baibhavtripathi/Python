mydict={}
while(True):
    try:
        a,b = input().split()
        mydict[a]= int(b)
    except:
        break
print(mydict)
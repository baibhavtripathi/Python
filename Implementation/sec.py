eart_p = int(input())
lat_degj = float(input())

x = (eart_p/360)*lat_degj
y = int(x)
l=[0]*2
#print(y)
if x>6.00 and x<=12.00:
    l[0]= (12.00-x)*30
elif x>12.00:
    l[0]= (x-12.00)*30
else:
    l[0] = x*30
y = x-y
l[1] = y*60*6
print('l0=',l[0],'l1=',l[1])
z = abs(l[0]-l[1])%360
if z> 180.00:
    print(format(360.00-z,'0.2f'),end='')
else:
    print(format(z,'0.2f'),end='')

#print(format(z%360,'0.2f'),end='')
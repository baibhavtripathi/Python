l = [i for i in range(1,101)]
i = 1
while len(l) != 1:
	l.pop(i)
	l.append(l[0])
	l = l[1:]
print(l)
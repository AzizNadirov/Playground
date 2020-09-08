s = 0
for i in range(2, 101):
	if i % 2 == 0:
		s = s + i
		print('i:',i, 's:',s)
print(s)
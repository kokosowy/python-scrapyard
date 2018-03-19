#!/usr/bin/env python3

a = '1435322412'

"""
for x in a:
	c = int(x)
	while c:	
		print('x',end='')
		c = c - 1
	print('')

###

j = 9
while j >= 0:
	i=0
	while i < 10:
		if int(a[i]) > j :
			print('x',end='')
		else:
			print(' ',end='')
		i+=1
	j-=1
	print('')
		
"""

j = 9
for j in range (9, -1, -1):
	for i in range(10):
		if int(a[i]) > j :
			print('x',end='')
		else:
			print(' ',end='')
	print()

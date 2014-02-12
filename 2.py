#Find the sum of all the even-valued terms in the sequence which do not exceed four million.

sum = 0
a, b = 0, 1
while b <= 4000000:
	a, b = b, a + b
	if b % 2 == 0:
		sum += b
		#print(b," added")
	#else: print(b)

print(sum)

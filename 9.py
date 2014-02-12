#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

limit = 1000

for a in range(1,limit):
	for b in range(a,limit):
		for c in range(b,limit):
			if a*a + b*b == c*c:
				#print("%d² + %d² = %d² is triple"%(a,b,c))
				if a+b+c == 1000:
					print("Found: %d, %d, %d"%(a,b,c))

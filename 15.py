import math

def fac(n):
	if n == 0:
		return 1
	else: return n*fac(n-1)

n = (fac(40)/(fac(20)*fac(20)))

print(int(n))

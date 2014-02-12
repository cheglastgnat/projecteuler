from functions import fac
from math import ceil

def bincoeff(n, k):
	return ( fac(n) / ( fac(k) * fac(n - k) ) )

result = 0

for n in range(1, 101):
	for r in range(0, ceil(n / 2)):
		if bincoeff(n, r) > 1000000:
			result += ( n - 2 * r ) + 1
			print("breaking at ({}, {}), adding {} to result".format(n, r, n-2*r+1))
			break

print("result: {}".format(result))

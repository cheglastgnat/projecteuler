from math import sqrt

def prime(n):
	if n == 0 or n == 1:
		return False
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def fac(n):
	if n == 0:
		return 1
	else: return n*fac(n-1)

def divisorsum(i):
	d = 0
	j = 1
	while j < i:
		if i % j == 0:
			d += j
		j += 1
	return d

def fold(neutral, function, iterator):
	if len( iterator ) == 0: return neutral
	else: return function( iterator[0], fold( neutral, function, iterator[1:] ) )


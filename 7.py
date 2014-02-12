#What is the 10001st prime number?
from math import sqrt
nth = 1

def prime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

x = 1

while nth < 10002:
	x += 1
	if prime(x):
		print(x,"is prime #%d"%nth)
		nth += 1
	else:
		print(x,"is not prime")


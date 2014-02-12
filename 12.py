# What is the value of the first triangle number to have over five hundred divisors?
from math import sqrt
from functions import prime

divisors_to_find = 5
candidate =2505 
euler = 1

def number_of_divisors(n):
	result = 1
	if prime(n): return result
	#divisors = []
	for div in range(1, int(sqrt(n))):
		if n % div == 0:
			result += 1
			#divisors.append(div)
	#print("%d has %d divisors: %s"%(n, result, divisors))
	return result*2

num = number_of_divisors(euler)
while num <= 500:
	candidate += 1
	euler = int(candidate*(candidate+1) / 2)
	num = number_of_divisors(euler)
	print("Testing: %d for %d has %d divisors" % (euler, candidate, num))
else:
	print(num,euler)



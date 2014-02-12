#Find the sum of all the primes below two million.

from functions import prime

sum = 0

for candidate in range(2,2000000):
	if prime(candidate):
		sum += candidate
		print("%d was a prime."%candidate)

print(sum)





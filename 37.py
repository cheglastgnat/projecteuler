#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

from functions import prime

stopcodons = set([0,4,6,8,9])
truncatable_primes = []
found = 0
number = 10

while found < 11:
	if number % 10000 == 0: print("{} searched".format(number))
	number += 1
	if number % 10 in stopcodons: continue
	s = str(number)
	while s:
		if prime(int(s)):
			s = s[1:]
		else:
			break
	else:
		s = str(number)
		while s:
			if prime(int(s)):
				s = s[:-1]
			else: break
		else:
			print("found one!")
			found += 1
			truncatable_primes.append(number)
else:
	print(found,"found:",truncatable_primes,"with sum",sum(truncatable_primes))




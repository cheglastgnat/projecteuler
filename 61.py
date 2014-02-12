#!/usr/bin/python3.1

# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.


def number(i, n):
	if i == 3:
		return(n*(n+1)/2)
	if i == 4:
		return(n**2)
	if i == 5:
		return(n*(3*n-1)/2)
	if i == 6:
		return(n*(2*n-1))
	if i == 7:
		return(n*(5*n-3)/2)
	if i == 8:
		return(n*(3*n-2))


def find_chain(found_indices, numbers):
	
	if len(found_indices) == 6 and numbers[0]//100 == numbers[-1]%100:  #six found and they are cyclic
		print(numbers)
		print(sum(numbers))
		print(found_indices)

	prefix = numbers[-1] % 100  #next number has to start with this prefix

	if prefix < 10: return False  #unfit prefix, won't generate a 4-digit next number

	for i in range(3, 8):
		if i in found_indices:
			continue
		n = 1
		while number(i, n) < 100*prefix:
			n += 1
		while number(i, n) < 100*(prefix+1):
			find_chain(found_indices+[i], numbers+[int(number(i, n))])
			n += 1


start = 1
while number(8, start) < 1000:
	start += 1

while number(8, start) < 10000:
	find_chain([8], [number(8, start)])
	start += 1


from functions import prime

primes = [2]

def primefactors(n):
	global primes
	while primes[-1] < n:
		i = primes[-1] + 1
		while not prime(i): i += 1
		else: primes.append(i)

	i = 0
	result = 0
	new = True

	while n > 1:
		if n % primes[i] == 0:
			n /= primes[i]
			if new:
				result += 1
				new = False
		else:
			i += 1
			new = True

	return result


found = 0
firstone = 0
candidate = 80001

while found < 4:
	if candidate % 1000 == 0: print("testing",candidate)
	candidate += 1
	if primefactors(candidate) == 4:
		if found == 0:
			firstone = candidate
		if found == 2: print("oh well...")
		if found == 3: print("almost there...")
		found += 1
	else:
		found = 0

print("yessir! found",firstone)

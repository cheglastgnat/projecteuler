from functions import prime

def interleave(l, new):
	for i, elem in enumerate(l):
		elem[i:i] = [new]
	l.reverse()
	return l


at_digit = 0
permlist = [[0]]

while at_digit < 7:
	print("interleaving digit {}".format(at_digit+1))
	l = []
	for perm in permlist:
		newlist = [perm[:] for i in range(at_digit+2)]
		interleave(newlist, at_digit+1)
		l.extend(newlist)
	permlist = l
	at_digit += 1

print("now sorting")
permlist.sort()



highest_pandigital_prime = 0

for i,perm in enumerate(permlist):

	if perm[0] != 0: 
		print("reached end of 1-9 pandigitals between {} and {}".format(permlist[i-1],perm))
		break

	candidate = int("".join([str(i) for i in perm]))

	if i % 10000 == 0: print("testing",i,candidate)

	if prime(candidate):
		print("found a prime:",candidate)
		if candidate > highest_pandigital_prime:
			highest_pandigital_prime = candidate
			print("found higher",candidate)

print(highest_pandigital_prime)

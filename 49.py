from functions import prime
import time

def get_permutations(prime):
	k = 0
	perms = []
	elems = [i for i in str(prime)]
	elems.sort()
	perms.append(int("".join([str(i) for i in elems])))
	while True:
		for i in range(len(elems)-2, -1, -1):
			if elems[i] < elems[i+1]:
				k = i
				break
		else:
			return perms
		for i in range(len(elems)-1, -1, -1):
			if elems[i] > elems[k]:
				elems[i], elems[k] = elems[k], elems[i]
				elems[k+1:] = elems[:k:-1]
				perms.append(int("".join([str(i) for i in elems])))
				break


found = []

for number in range(1000,9999):
	if not prime(number): continue

	i = get_permutations(number)
	perms = []
	for n in i:
		if n%2==0: continue
		if prime(n): perms.append(n)

	if len(perms) < 3 or perms[0] < 1000: continue
	
	for i,p in enumerate(perms):
		for q in perms[i+1:]:
			if q+(q-p) in perms: 
				if p in found: break
				else:
					print(p,q,2*q-p)
					found.append(p)







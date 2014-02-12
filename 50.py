from functions import prime
import time


def eratosthenes(debug=False):
	numbers = [i for i in range(2,1000000)]
	for i in numbers:
		if i==0: continue
		j = i
		while i*j < len(numbers):
			numbers[i*j-2] = 0
			j += 1
	ls = [x for x in numbers if x!=0]
	return ls[:-2]


primes = []
#print("testing method 2")
#start = time.clock()
primes = eratosthenes()
#end = time.clock()
#print("method 2 ran {} seconds, gave {} primes".format(end-start,len(primes)))


longestchain = 0
primo = 0
primeset = set(primes)

for i,start in enumerate(primes):
	if i%8000==0: 
		print(i,"done")
	if 78498 - i - 1 < longestchain: continue
	n = 0
	currentchain = longestchain
	for x in range(i, i+longestchain+1):
		n += primes[x]
	for x in range(i+longestchain+1, len(primes)-1):
		currentchain += 1
		n += primes[x]
		if currentchain%2==1: continue
		if n >= 1000000: break
		if n in primeset and currentchain > longestchain:
			print("found longer chain, longest chain has {} elements".format(currentchain))
			longestchain = currentchain
			primo = n
	
print(longestchain,primo)

#!/usr/bin/python3.1

from functions import prime

testset = set()
tens = [10**i for i in range(0,30)]

def test(n, debug=False):
	global tens
	s = str(n)
	maxprimes = 7 	#accelerate the program, should be 0 in general case
	for i in range(1, 2**(len(s))):
		#if "{0:b}".format(i)[:-1] == '1': continue	#if the last digit is to be changed, not enough primes can be generated
		if i%2==1: continue #same, but probably faster :P
		primes = 0
		for z in range(0,10):
			if 10-z+primes < maxprimes: break #there are not enough prime candidates left, so give up
			tester = sum( [ n*tens[i] for i,n in enumerate([ (z if char == '1' else int(s[u])) for u,char in enumerate("{0:{a}{f}{l}b}".format(i,f='0',a='>',l=len(s))) ][::-1]) ] )
			if z == 0 and len(str(tester)) < len(s): continue #is this allowed or not?
			if tester in testset:
				primes += 1
				if debug: print(tester)
			elif prime(tester):
				primes += 1
				if debug: print(tester)
				testset.add(tester)
		if primes > maxprimes: maxprimes = primes
		if debug: print("----------")
	return maxprimes



i = 10

while True:
	i += 1
	while not prime(i):
		i+=1
	t = test(i)
	if t >= 8:
		break
	else:
		print("testing {} failed: maximum family size {}".format(i,t))

print("{} was found: {}!".format(i,t))
test(i, True)



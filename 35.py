from functions import prime

def next_permutation(s):
	if len(s) == 1: return s
	else: return s[1:]+s[:1]


primesbuffer = set()
circularprimes = set()

for candidate in range(2,1000000):
	if candidate % 10000 == 0: print("{}% done".format(candidate // 10000))
#	print("candidate is",candidate)
	string = str(candidate)
#	print(string)
	for i in range(len(string)):
		string = next_permutation(string)
#		print("permutation",string)
		c = int(string)
		if c in primesbuffer:
#			print(c,"was in buffer")
			continue
		elif prime(c):
#			print(c,"is prime and was not in buffer")
			primesbuffer.add(c)
		else:
#			print(c,"is not a prime")
			break
	else:
		circularprimes.add(candidate)

print(len(circularprimes),circularprimes)


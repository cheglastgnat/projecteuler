#Which starting number, under one million, produces the longest chain?

def step(n):
	if n % 2 == 0:
		#n even
		return n // 2
	else:
		#n odd
		return 3*n + 1

def chain(n):
	steps = 0
	while n > 1:
		steps += 1
		n = step(n)
	return steps

maxsteps = 0
maxcandidate = 0
for x in range(1000000):
	tmp = chain(x)
	if tmp > maxsteps:
		maxsteps = tmp
		maxcandidate = x
		print("Now at %d, new max chain length is %d." %(x, maxsteps))
else: print("Reached 999999, max chain length was %d at %d." % (maxsteps, maxcandidate))



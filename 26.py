

def getcycle(divisor):
	rest = 1
	rests = [] #keep track of seen result rests
	
	while True: #will be broken to exit
		while rest < divisor:
			rest *= 10 #go to next division step
	
		rest = rest % divisor #acquire next result rest
		if rest == 0: return 0 #clean division -> no cycle

		for i,r in enumerate(rests):
			if r == rest: return len(rests)-i #rest revisited -> cycle found

		rests.append(rest)


maxcycle, maxdivisor = 0, 0
for i in range(1,1000):
	if getcycle(i) > maxcycle:
		maxdivisor = i
		maxcycle = getcycle(i)

print("longest cycle was {}-digits recurring on 1/{}".format(maxcycle, maxdivisor))

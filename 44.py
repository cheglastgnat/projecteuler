

def next_pentagonal():
	n = 0
	while True:
		n += 1
		yield int(n*(3*n - 1) / 2)


generator = next_pentagonal()

pentagonals = [next(generator) for i in range(10)]

#print(pentagonals)i
minimumdistance = -1
breakoff = False
countA,countB,countC,countD = 0,0,0,0

for i,Pk in enumerate(pentagonals):
	countA += 1
	if countA % 100 == 0: print("at Pk #{}, {} sums hit, {} differences hit, {} both".format(countA,countB,countC,countD))
	if breakoff: break
	for j,Pj in enumerate(pentagonals):
		if Pj >= Pk: break

		while Pj + Pk > pentagonals[-1]:
			x = next(generator)
			pentagonals.append(x)

		csum = Pj + Pk
		cdif = abs(Pj - Pk)
		if cdif < minimumdistance and i==j+1: breakoff = True
		if cdif in pentagonals: countC += 1

		if csum in pentagonals:
			countB += 1
			if cdif in pentagonals:
				countD += 1
				if cdif < minimumdistance or minimumdistance == -1:
					minimumdistance = cdif
					print("found new low",minimumdistance)


print(minimumdistance)

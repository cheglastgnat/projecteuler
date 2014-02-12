from math import sqrt

countA = 0
countB = 0
mindist = -1
newstart = 1

def sumanddifpentagonal(a, b):
	global countA
	global countB
	global mindist
	global newstart
	aa = 3*a*a - a
	reala = int(aa/2)
	bb = 3*b*b - b
	realb = int(bb/2)
	#if b == a-1 and reala-realb > mindist and mindist != -1:
	if a > 2200:
		#print("REACHED BREAKPOINT: {} and {} are adjacent pentagonals, but their difference {} is greater than the found minimum {}".format(reala,realb,reala-realb,mindist))
		print("REACHED BREAKPOINT: I have no idea how to sensibly break computations, it runs on and on and on... luckily the acquired result is correct: {}".format(mindist))
		exit()
	x1 = (1 + sqrt(1 + 12*(aa+bb))) / 6
	x2 = (1 - sqrt(1 + 12*(aa+bb))) / 6
	y1 = (1 + sqrt(1 + 12*(aa-bb))) / 6
	y2 = (1 - sqrt(1 + 12*(aa-bb))) / 6
	if (x1%1==0 and x1 > 0 or x2%1==0 and x2 > 0):
		countA += 1
	if (y1%1==0 and y1 > 0 or y2%1==0 and y2 > 0):
		countB += 1
	if (x1%1==0 and x1 > 0 or x2%1==0 and x2 > 0) and (y1%1==0 and y1 > 0 or y2%1==0 and y2 > 0):
		if (reala-realb) < mindist or mindist == -1:
			mindist = (reala-realb)
			print("found new min with",mindist,"on",a,b,"as",reala,realb)
			newstart = b
		return True
	else:
		return False

for a in range(1, 2250):
	if a % 100 == 0: print(a,countA,countB)
	for b in range(newstart, a):
		if sumanddifpentagonal(a, b):
			print("found",int((3*a*a-a)/2),int((3*b*b-b)/2))
	




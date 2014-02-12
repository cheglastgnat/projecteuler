from math import sqrt

def tri(n):
	return int((a*a+a)/2)

def ispenta(n):
	s = sqrt(1 + 24*n)
	x1 = (1 + s)/6
	x2 = (1 - s)/6
	if (x1%1==0 and x1 > 0) or (x2%1==0 and x2 > 0):
		return True
	else:
		return False

def ishexa(n):
	s = sqrt(1 + 8*n)
	x1 = (1 + s)/4
	x2 = (1 - s)/4
	if (x1%1==0 and x1 > 0) or (x2%1==0 and x2 > 0):
		return True
	else:
		return False


a = 285
found = False

while not found:
	a += 1
	tria = tri(a)
	if ispenta(tria) and ishexa(tria):
		found = True
else:
	print("found it! at position {} is triangle number {}".format(a, tria))

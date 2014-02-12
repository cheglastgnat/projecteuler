#!/usr/bin/python3.1

#how many Lychrel numbers are there below 10.000?

import functions, itertools

def isLychrel(n):
	level = 0
	while level < 50:
		level += 1
		n += int(str(n)[::-1])
		if str(n) == str(n)[::-1]:
			return False
	return True


found = 0
for i in range(1,10000):
	if isLychrel(i):
		found += 1
		print("found {}".format(i))

print("found {} Lychrel numbers <10000".format(found))


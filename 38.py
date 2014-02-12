def ispandigital(n):
	if len(n) != 9:
		return False
	digitset = set()
	for char in n: digitset.add(char)
	if len(digitset) == 9 and not '0' in digitset:
		return True
	else:
		return False


largestpandigital = 0

for number in range(1,50000):
	s = ""
	n = 1
	while len(s) < 9:
		s = s + str(n * number)
		n += 1
	if len(s) == 9:
		if ispandigital(s):
			print("found",s,"for",number)
			if int(s) > largestpandigital:
				largestpandigital = int(s)
	else:
		continue

print(largestpandigital)


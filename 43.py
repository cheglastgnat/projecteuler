import pickle

f = open('24permutations','rb')
numbers = pickle.load(f)
f.close()
print("list of pandigitals loaded from",f)

divisors = [2,3,5,7,11,13,17]

running = 0
sum = 0

for number in numbers:

	if running % 35500 == 0: print("now at {}%".format(running // 35500))
	running += 1

	#numbers starting with 0 are not 0-9 pandigital
	if number	[0] == 0:
		continue

	s = "".join([str(i) for i in number])

	for i in range(7):
		if int(s[i+1:i+4]) % divisors[i] != 0:
			break
	else:
		print("found one!", s)
		sum += int(s)

print(sum)

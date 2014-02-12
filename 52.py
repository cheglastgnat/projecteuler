import itertools

def is_permutation_of(a, b):
	if len(a) != len(b): return False
	for chara in a:
		for i,charb in enumerate(b):
			if chara == charb: 
				del b[i]
				break
	return (len(b) == 0)

number = 1

while True:
	number += 1
	if number % 10000 == 0: print("now at {}".format(number))
	n = [c for c in str(number)]
	if int(n[0]) >= 2:
		i = 10
		while i < number: i *= 10
		number = i
	for i in range(2,7):
		if not is_permutation_of([c for c in str(i*number)], n[:]):
			break
	else: break

print(number)

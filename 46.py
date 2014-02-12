from functions import prime

number = 31
goldbach = True

while goldbach:
	number += 2
	if number % 1001 == 0: print("testing",number)
	if prime(number): continue

	for n in range(1, number):
		if 2*n*n > number: continue
		if prime(number - 2*n*n): break
	else:
		goldbach = False

print("Goldbach was wrong! {} is odd composite, but not decomposable!".format(number))



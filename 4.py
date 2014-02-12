#Find the largest palindrome made from the product of two 3-digit numbers.

biggestyet = 1

for x in range(800,1000):
	for y in range(800,1000):
		i = str(x*y)
		if i == i[::-1]:
			biggestyet = max(biggestyet, x*y)

print(biggestyet)



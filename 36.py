#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

sum = 0

for i in range(1000000):
	if str(i) == str(i)[::-1] and str(bin(i))[2:] == str(bin(i))[:1:-1]:
		print("found",i,bin(i))
		sum += i

print(sum)

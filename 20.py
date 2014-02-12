#Find the sum of the digits in the number 100!

from functions import fac

pool = str(fac(100))
print(fac(100))

sum = 0

for char in pool:
	sum += int(char)

print(sum)



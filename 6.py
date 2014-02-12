#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

limit = 100

sumsquare, squaresum = 0, 0

for i in range(1,limit+1):
	sumsquare += i
	squaresum += i*i

sumsquare *= sumsquare

print(sumsquare-squaresum)



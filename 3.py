#What is the largest prime factor of the number 600851475143 ?

number = 600851475143

divisor = 2

while divisor <= number:
	if number % divisor == 0:
		print(divisor, "is prime factor")
		number /= divisor
	divisor += 1

print(number, "remains")

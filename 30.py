sum = 0

def mysum(list):
	sum = 0
	for elem in list:
		sum += elem
	return sum

for number in range(2,1000000):
	if number % 100000 == 0: print("checkpoint!",number)
	if mysum([int(char)**5 for char in str(number)]) == number:
		print("found",number)
		sum += number

print(sum)


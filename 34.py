from functions import fac

def mysum(list):
	sum = 0
	for elem in list:
		sum += elem
	return sum

sum = 0

for i in range(3,2500000):
	if i % 25000 == 0:
		print("{}% done".format(i // 25000))
	if i == mysum([fac(int(char)) for char in str(i)]):
		sum += i
		print("found",i)

print(sum)



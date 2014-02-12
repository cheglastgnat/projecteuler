a = []
b = []

for i in range(1,10001):
	a.append(i)

def d(i):
	divisorsum = 0
	j = 1
	while j < i:
		if i % j == 0:
			divisorsum += j
		j += 1
	return divisorsum


#for i in a:
#	if i%100==0: print("now at",i)
#	b.append(d(i))


amicablesum = 0

for i in a:
	if d(i) > 9999: continue
	if d(d(i)) == i and d(i) != i: 
		print("amicable numbers:",i,d(i))
		print("adding:",i)
		amicablesum += i


print(amicablesum)





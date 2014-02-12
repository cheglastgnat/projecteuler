import time

totalnumerator = 1
totaldenominator = 1

starttime = time.clock()

for denominator in range(10,100):
	denominatorset = set([denominator // 10, denominator % 10])

	for numerator in range(10, denominator):
		numeratorset = set([numerator // 10, numerator % 10])
#		print(numeratorset,denominatorset)

		for i in numeratorset:
			if i in denominatorset:
				if i == 0: continue
				a = numeratorset.copy()
				if len(a) > 1:
					a.remove(i)
				b = denominatorset.copy()
				if len(b) > 1:
					b.remove(i)
				x = a.pop()
				y = b.pop()
				if y == 0: continue
				if (x/y)==(numerator/denominator):
					totalnumerator *= numerator
					totaldenominator *= denominator
					print("found: {}/{} = {}/{}".format(numerator,denominator,x,y))
					break

endtime = time.clock()

print(totalnumerator,totaldenominator,endtime-starttime)




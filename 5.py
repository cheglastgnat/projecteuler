#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#2432902008176640000
import time

number = 20
notfound = True

starttime = time.clock()

while notfound:
	number += 20 
	if number % 1000000 == 0: print("Testing", number)
	notfound = False
	for i in range(1,21):
		if notfound: break
		if number // i != number / i:
			#print("not ",i)
			notfound = True
	
endtime = time.clock()

print("Found:",number,"in",endtime-starttime,"seconds")



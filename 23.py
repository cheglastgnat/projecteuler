from functions import divisorsum
import pickle

#abundants = []

#for i in range(28123):#28123
#	if i % 1000 == 0: print("testing",i)
#	d = divisorsum(i)
#	if i < d:
#		abundants.append(i)
#		print("added",i,"with",d,"to abundants")

f = open('23abundants','rb')
#pickle.dump(abundants,f)
#print("saved to",f)
abundants = set(pickle.load(f))
print("loaded from",f)
f.close()


startnumber = 0
numsum = 0

while startnumber <= 28123:
	#print("now at",startnumber)
	for a in abundants:
		if a > startnumber/2 or a > 14112: 
			numsum += startnumber
			print(startnumber,"found one! sum is now",numsum)
			break
		if (startnumber-a) in abundants:
			print(startnumber,"is sum of",a,startnumber-a)
			break	
	else:
		numsum += startnumber
		print("found one!! sum is now",numsum)
	startnumber += 1

print(numsum)



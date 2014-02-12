import pickle


f = open('24permutations', 'br')
permlist = pickle.load(f)
f.close()
print("loaded permutations from",f)
#permlist = [[0,1,4,3,2,9,8,7,6,5]]

productset = set()

for i,perm in enumerate(permlist):
	if perm[0] != 0:
		print("reached end of 1-9 pandigitals between {} and {}".format(permlist[i-1],perm))
		break
	
	if i % 3500 == 0:
		print("about {}% done".format(i // 3500))
	
	for firstcut in range(1,7):
		for secondcut in range(firstcut+1,8):
			p = "".join([str(i) for i in perm]) 
			a = int(p[:firstcut])
			b = int(p[firstcut:secondcut])
			c = int(p[secondcut:])
			if a * b == c:
			#if sum([10**(len(perm)-i-1) * j for i,j in enumerate(perm[:firstcut])]) * sum([10**(len(perm)-i-1) * j for i,j in enumerate(perm[firstcut:secondcut])]) == sum([10**(len(perm)-i-1) * j for i,j in enumerate(perm[secondcut:])]):
				productset.add(int(p[secondcut:]))
				print("found {}*{}={}".format(a,b,c))

print(sum(productset))



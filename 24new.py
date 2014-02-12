
import pickle


def interleave(l, new):
	#print("got list ",l)
	for i, elem in enumerate(l):
		#print("elem was",elem,i)
		elem[i:i] = [new]
		#print("elem now is",elem)
	l.reverse()
	#print("returning",l)
	return l


#at_digit = 0
#permlist = [[0]]

#while at_digit < 9:
#	print("interleaving digit {}".format(at_digit+1))
#	l = []
#	for perm in permlist:
#		newlist = [perm[:] for i in range(at_digit+2)]
#		interleave(newlist, at_digit+1)
#		l.extend(newlist)
#	permlist = l
#	at_digit += 1

#print("now sorting")
#permlist.sort()

#print("dumping list")
#f = open('24permutations','bw')
#pickle.dump(permlist,f)
#f.close()
#print("dumped to {}",f)

f = open('24permutations','br')
permlist = pickle.load(f)
f.close()
print("loaded list from",f)

print("millionth permutation is", permlist[999999])




f = open('words.txt','r')
names = [name[1:-1] for name in f.read().split(',')]
f.close()
print("names read from",f,"(first name is",names[0],")")

triangulars = [int(n*(n+1)/2) for n in range(1, 100)]
print(triangulars)
trianglewords = 0
maxv = 0

for name in names:
	namevalue = sum([ord(char)-64 for char in name])
	maxv = max(maxv,namevalue)
	if namevalue in triangulars:
#		print(name,"is triangular with value",namevalue)
		trianglewords += 1

print("max",maxv)
print("found {} triangle words".format(trianglewords))


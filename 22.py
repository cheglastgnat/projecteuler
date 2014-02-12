f = open('names.txt','r')

names = [name[1:-1] for name in f.read().split(',')]

names.sort()

listvalue = 0

for (index, name) in enumerate(names):
	print(index,listvalue)
	namevalue = 0
	for char in name:
		namevalue += ord(char)-64
	listvalue += (index + 1) * namevalue

print(listvalue)


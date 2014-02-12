i = 1
a, b = 0, 1

while len(str(b)) < 1000:
	i += 1
	a, b = b, a + b
else:
	print(b,"the fib number #",i,"has",len(str(b)),"digits")

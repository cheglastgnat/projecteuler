atdigit = 0
s = "0"
n = 0

while len(s) <= 1000000:
	n += 1
	s = s + str(n)


result = 1
for i in range(7):
	result *= int(s[10**i])
	print(s[10**i])

print(result)

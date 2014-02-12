results_p = {}

for i in range(1000):
	results_p[i] = 0

running = 0

for a in range(1, 1000):
	for b in range(a, 1000-a):
		for c in range(b, 1000-a-b):
			running += 1
			if running % 100000 == 0: print(running,"tested")
			if a+b+c <= 1000 and a*a+b*b==c*c:
				results_p[a+b+c] += 1


max_p = 0
max_v = 0
for i in results_p.keys():
	if results_p[i] > max_v:
		max_p = i
		max_v = results_p[i]

print(max_p)

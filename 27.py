
from functions import prime

high_a, high_b = 0, 0
max_chain = 0

for b in range(-999,1000):
	if not prime(abs(b)): continue

	for a in range(-999,1000):
		current_chain = 0
		n = 0
		while prime(abs(n*n + a*n + b)):
			n += 1
			current_chain += 1
		else:
			if current_chain > max_chain:
				print("found higher",a,b,max_chain)
				max_chain, high_a, high_b = current_chain, a, b

print(high_a, high_b, high_a*high_b)


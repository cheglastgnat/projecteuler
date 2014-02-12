#!/usr/bin/python3.1

#Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
import itertools

maxa = maxb = maxsum = 0

for a in range(100):
	print("now at base {}".format(a))
	for b in range(101):
		new = sum([ int(char) for char in str(a**b) ])
		if new > maxsum:
			maxa, maxb, maxsum = a, b, new

print(maxa, maxb, maxsum)

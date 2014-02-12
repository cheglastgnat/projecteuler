#!/usr/bin/python3

# what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

from functions import prime


ratio = 0.5
has_risen = False #b/c ratio starts at 0, the break condition checks whether it has already been > 0.1 at some time

x = y = 1
counter = 2
revolution = 1
number = 3
direction = 'left'
primes = 0

while True:
#for i in range(15):
	
	#number += 1

	#print(x,y,number,direction)
	
	counter += 1
	if abs(x) == abs(y):
		if prime(number): primes += 1
		ratio = primes/counter
		#if prime(number):primes.append(number)
		if ratio >= 0.1 and not has_risen: has_risen = True
		
	if direction == 'right':
		x += 2*revolution+1
		number += 2*revolution+1
		if x > revolution:
			ratio = primes/counter
			direction = 'up'
			if revolution%100==0:
				print("revolution {} finished, ratio is at {:.10f}%, {}/{}".format(revolution, ratio*100, primes, counter))
			if ratio < 0.1 and has_risen:
				break
			#if revolution >= 3:break
			revolution += 1
			continue
			
	elif direction == 'up':
		y += 2*revolution-1
		number += 2*revolution-1
		if y >= revolution:
			direction = 'left'
			continue
			
	elif direction == 'left':
		x -= 2*revolution
		number += 2*revolution
		if x == -revolution:
			direction = 'down'
			continue

	elif direction == 'down':
		y -= 2*revolution
		number += 2*revolution
		if y == -revolution:
			direction = 'right'
			continue


print("found {} primes in {} numbers, ratio is {:.10f}%, last revolution was {} with length {}".format(primes,
																									   counter,
																									   ratio*100,
																									   revolution,
																									   2*revolution+1))
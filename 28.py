
x, y = 0, 0
n = 1
direction = 0
limit = 1002001
diagonalsum = 0

while n <= limit:
	#print(x,y,direction)
	if x == y or x == -y:
		diagonalsum += n
		print(n,"at",diagonalsum)

	n += 1

	if direction == 0:
		x += 1
	elif direction == 1:
		y -= 1
	elif direction == 2:
		x -= 1
	else:
		y += 1

	if y == x-1 and x > 0:
		direction = 1
	elif x == -y and x > 0:
		direction = 2
	elif x == y and x < 0:
		direction = 3
	elif x == -y and x < 0:
		direction = 0

print(diagonalsum)




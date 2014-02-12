#!/usr/bin/python3.1

triangle = []
f = open('triangle.txt', 'r')
for line in f.readlines():
	triangle.append([int(n) for n in line[:-1].split(' ')])
f.close()


triangle.reverse()
        
def bestmove(x, y):
    triangle[y][x] += max(triangle[y-1][x], triangle[y-1][x+1])



for (y, line) in enumerate(triangle):
	if y == 0: continue #leaves have no policy
	for (x, elem) in enumerate(line):
		bestmove(x, y)

								    
for line in triangle: print(line)


#!/usr/bin/python3.1

import itertools

current_index = 1
cubes = {1}
max_cube = 1

def extend(n):
  global current_index, max_cube, cubes
  while max_cube < n:
    current_index += 1
    max_cube = current_index**3
    cubes.add(max_cube)
        

i = 10
while True:
  i += 1
  c = i**3
  cubes_found=0
  s = {int("".join(p)) for p in itertools.permutations([s for s in str(c)]) if p[0]!='0'}
  if len(s) < 5: continue
  for p in s:
    extend(p)
    if p in cubes: cubes_found += 1
  if i%10==0: print("checked",c,"as cube of",i,"with",cubes_found)
  if cubes_found == 5:
    print("found", c, "as cube of", i)
    exit(0)


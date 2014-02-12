#!/usr/bin/python

def group_of_cubes():
  cur_index = cur_len = 0
  while True:
    cubes = []
    cur_len += 1  #proceed to next length group
    while True:
      cur_index += 1
      next_cube = cur_index**3
      if len(str(next_cube)) != cur_len: 
        cur_index -= 1
        break
      cubes.append(next_cube)
    yield cubes

for (i, cubes) in enumerate(group_of_cubes()):
  cube_groups = {}
  for cube in cubes:
    p = [char for char in str(cube)]
    p.sort()
    p = "".join(p)
    if p in cube_groups.keys():
      cube_groups[p] += 1
    else:
      cube_groups[p] = 1
  l = cube_groups.keys()
  l.sort()
  for c in l:
    if cube_groups[c] == 5:    
      for cube in cubes:
        p = [char for char in str(cube)]
        p.sort()
        p = "".join(p)
        if p == c:
          print "Found {} as {}**3".format(cube,int(cube**(1./3)))
          exit(0)


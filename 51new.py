#!/usr/bin/pypy

from functions import prime
from itertools import chain, combinations

def powerset(it):
  s = list(it)
  return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

def extendprimes(p,i,m):
  while i <= m:
    if i in p or prime(i): p.add(i)
    i += 1

primes = set([1,2])
maxprime = 3
i = 3

while True:
  i += 2
  if len(str(i))>len(str(i-2)): 
    primes = set()
    print "set cleared" 
  if i%1001==0: print "testing",i 
  if i not in primes and not prime(i): continue
  for positions in powerset(range(len(str(i)))):
    if len(positions) == 0 or len(str(i))-1 in positions: continue
    famsize = 0  # i itself is always in the family
    family = []
    for lit in range(10):
      if 0 in positions and lit == 0: continue
      new = list(str(i))
      for p in positions: new[p] = str(lit)
      new = int("".join(new))
      if new in primes or (prime(new) and not primes.add(new)):
        famsize += 1
        family.append(new)
    if famsize == 8 and i in family:
      print i,", replacing positions",positions,", generates",family 
      exit(0)


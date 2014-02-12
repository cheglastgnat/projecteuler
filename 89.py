#!/usr/bin/python

import functools

def read_number(string):
  """Converts a Roman-literal number string into an Integer"""
  literals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
  as_literals = [literals[char] for char in string]
  n = [(a if a>=b else -a) for (a,b) in zip(as_literals[:-1],as_literals[1:])] + [as_literals[-1]]
  n = functools.reduce((lambda a,b:a+b), n)
  return n

def translate_number(n):
  """Converts an integer number into a Roman-literal 
  number string of minimum length"""
  literals = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
  p = sorted(literals.keys())[::-1]
  s = []
  while n > 0:
    for l in p:
      if n >= l:
        n -= l
        s.append(literals[l])
        break
  return "".join(s)
  

if __name__ == '__main__':

  f = open('roman.txt','r')
  raws = [line.strip() for line in f]
  f.close()

  numbers = [read_number(n) for n in raws]
  minimized = [translate_number(s) for s in numbers]

  l1 = sum([len(s) for s in raws])
  l2 = sum([len(s) for s in minimized])
  for (n,a,b) in zip(numbers,raws, minimized):
    print "({0}) {1} -> {2}, saved {3} chars".format(n,a,b,len(a)-len(b))
  print "Saved {0} chars in conversion ({1} -> {2})".format(l1-l2,l1,l2)

  


#!/usr/bin/python3

# In the first one-thousand expansions of the sqrt(2) continued fraction,
# how many fractions contain a numerator with more digits than denominator?


#fractions_as_strings = [ ( "(1+1/" + "(2+1/"*(i-1) + "2" + ")"*i ) for i in range(1, 1001)]
#for i in range(4): print(fractions_as_strings[i], eval(fractions_as_strings[i]), float.as_integer_ratio(eval(fractions_as_strings[i])))


numerator, denominator = 1, 2
target_counter = 0

for i in range(1000):
	#print(numerator, denominator)
	numerator, denominator = denominator, numerator + 2 * denominator
	if len(str(numerator+denominator)) > len(str(denominator)):
		target_counter += 1

print("numerator had more digits than denominator in {} iterations".format(target_counter))
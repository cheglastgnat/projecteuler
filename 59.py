#!/usr/bin/python3

# Using a brute force attack, can you decrypt the cipher using XOR encryption?


# generates the potential keys on-demand
def generated_keys():
	for a in range(97, 123):
		for b in range(97, 123):
			for c in range(97, 123):
				yield [a, b, c]


def decrypt(key):
	f = open('cipher1.txt', 'r')
	cipher = tuple([ int(cell) for cell in f.readline().strip().split(',') ])
	f.close()

	cleartext = []
	clearnumbers = []

	for ( i , atom ) in enumerate(cipher):
		c = atom ^ key[i%3]
		clearnumbers.append( c )
		cleartext.append( chr( c ) )

	print(''.join(cleartext))
	print("sum of plaintext ascii is", sum(clearnumbers))

decrypt([103,111,100])
print("The key was [{}]".format(''.join([chr(i) for i in [103,111,100]])))
exit()

# read in the provided cipher text as numbers
# plaintext contains only english words
f = open('cipher1.txt', 'r')
cipher = tuple([ int(cell) for cell in f.readline().strip().split(',') ])
f.close()

# comparative table of single-letter frequencies for frequency-analysis deciphering approach
# taken from ["Cryptanalysis", Helen Gaines]
frequencies = (7.81, 1.28, 2.93, 4.11, 13.05,
               2.88, 1.39, 5.85, 6.77,  0.23,
               0.42, 3.60, 2.62, 7.28,  8.21,
               2.15, 0.14, 6.64, 6.46,  9.02,
               2.77, 1.00, 1.49, 0.30,  1.51, 0.09)

good_distances = [0,0,0,0,0]
good_keys      = [0,0,0,0,0]

index = 0

for key in generated_keys():

	index += 1
	if index%1700==0: print("{:.0%} of possible keys tested".format(index/17576))
	
	cleartext    = []
	clearnumbers = []

	# retrieve plaintext
	for ( i , atom ) in enumerate(cipher):
		c = atom ^ key[i%3]
		clearnumbers.append( c )
		cleartext.append( chr( c ) )

	# compute single-letter frequencies
	test_frequencies = [ 0 for i in range(26) ]
	letters = 0
	for number in clearnumbers:
		if 97 <= number <= 122:
			test_frequencies[number - 97] += 1
			letters += 1
	for ( i , ignore ) in enumerate(test_frequencies):
		test_frequencies[i] /= letters

	# good candidate keys generate a single-letter frequency very like the reference (Euclid distance)
	distance = sum( [ abs(a-b)**2 for (a,b) in zip(test_frequencies, frequencies) ] )
	
	for ( i , ref ) in enumerate(good_distances):
		inserted = False
		if distance < ref or ref == 0 and not inserted:
			good_distances.insert(i, distance)
			good_distances[5:] = []
			good_keys.insert(i, key)
			good_keys[5:] = []
			inserted = True

	#print(key, ''.join(cleartext), sum(clearnumbers))

print(good_distances, good_keys)
		




from functions import fac

coins = [200,100,50,20,10,5,2,1]
#combs = 0
memo = {}

def combinations(pennies, depth=0, use_array=False, currentcoin=200):

	if use_array:
		if pennies in memo: 
			return memo[pennies]

	sum = 0

	if pennies == 0 or currentcoin == 1: 
		#global combs 
		#combs += 1
		return 1

	counted = 0
	for coin in coins:
		if coin <= pennies and coin <= currentcoin:
			counted += 1
			sum += combinations(pennies - coin, depth+1, use_array, coin)

	return sum


#for i in range(1, 20):
#	x = combinations(i)
#	memo[i] = x
#	print("found {} combinations for {}".format(x, i))
#
#for i in range(20,40):
#	x = combinations(i,0,True)
#	memo[i] = x
#	print("found {} combinations for {}".format(x, i))
#
#for i in range(40,190):
#	x = combinations(i,0,True)
#	memo[i] = x
#	print("found {} combinations for {}".format(x, i))



x = combinations(200, 0, False)
print(x)

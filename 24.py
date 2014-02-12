from functions import fac

resultlist = [-1 for i in range(10)]
number = 1000000
digit = 9

while number > 0:
	if digit < 0:
		break
	x = fac(digit)
	if x <= number:
		print(x,"fits still in",number,", digit is",digit)
		number -= x
		while resultlist[digit] in resultlist[:digit] or resultlist[digit] in resultlist[digit+1:] or resultlist[digit] == -1:
			resultlist[digit] += 1
		resultlist[digit] += 1
		a = resultlist[:]
		a.reverse()
		print("".join([str(i) for i in a]))
	else:
		digit -= 1

resultlist.reverse()
print("".join([str(i) for i in resultlist]))





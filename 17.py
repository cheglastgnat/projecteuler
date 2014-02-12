ones = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
tens = ["gnarf","one","twen","thir","for","fif","six","seven","eigh","nine"]

def one_number(n):
	if n == 1000:
		return "onethousand"
	elif 99 < n < 1000:
		digit = n // 100
		rest = n - 100*digit
		if rest == 0:
			return ones[digit] + "hundred"
		else:
			return ones[digit] + "hundredand" + one_number(rest)
	elif 19 < n < 100:
		digit = n // 10
		rest = n - 10*digit
		return tens[digit] + "ty" + ones[rest]
	elif 12 < n:
		rest = n - 10
		return tens[rest] + "teen"
	elif n == 11: return "eleven"
	else: return ones[n]

sum = 0
for i in range(1,1001):
	sum += len(one_number(i))
	print(one_number(i))

print(sum+10)


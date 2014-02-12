totaldays = 0
month = 1
year = 1900

sundays = 1

days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

while year <= 2000 and month <= 12:
	if month == 2:
		totaldays += (lambda x: 29 if year%400==0 else (28 if year%100==0 else (29 if year%4==0 else 28)))(year)
	else:
		totaldays += days[month]
	month += 1
	if month == 13:
		month = 1
		year += 1
	if totaldays % 7 == 0 and year > 1900:
		sundays += 1
		print("Sunday on 1",month,year)

print(sundays)



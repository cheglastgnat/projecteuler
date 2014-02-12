import re
import urllib.request
import contextlib

regex = re.compile(r'[\d]{50}')
url = 'http://projecteuler.net/index.php?section=problems&id=13'

with contextlib.closing(urllib.request.urlopen(url)) as source:
	data = source.read().decode('ascii')
	numbers = re.finditer(regex, data)

	sum = 0
	for match in numbers:
		sum += int(match.group())
	print(sum)
	print("First ten digits are", str(sum)[:10])



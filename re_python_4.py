import re

test_string = 'hello123'

pattern = re.compile(r'_?\d')
matches = pattern.finditer(test_string)
for match in matches:
	print(match)

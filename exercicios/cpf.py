import re

string = '488.252.688-31'
pattern = re.compile('[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}')
x = re.fullmatch(pattern, string)
print(x)
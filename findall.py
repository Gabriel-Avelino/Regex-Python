import re

string1 = 'Gabriel Gabriel'

pattern = re.compile('Gabriel')

# findall: Pega todas as vezes que um caractere se encontra naquela string.
x = re.findall(pattern, string1)

print(x)  # ['Gabriel', 'Gabriel']


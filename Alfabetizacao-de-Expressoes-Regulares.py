# Para entender as verificações abaixo, abra o arquivo do Dicionário de expressões regulares: 
import re

# Teste 1.1
string1 = 'Gabriel'

pattern1 = re.compile('.......')

a = re.fullmatch(pattern1, string1)

print(a)  # <re.Match object; span=(0, 7), match='Gabriel'>

# Teste 1.2
string2 = 'Gabriel'

pattern2 = re.compile('Ca.....')  

b = re.fullmatch(pattern2, string2)

print(b)  # None

# Teste 2
string3 = 'Gabriel.'

pattern3 = re.compile('.......\.')

c = re.fullmatch(pattern3, string3)

print(c)  # <re.Match object; span=(0, 8), match='Gabriel.'>
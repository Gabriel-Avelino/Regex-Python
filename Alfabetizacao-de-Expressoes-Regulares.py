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

# Teste 3
string4 = 'avelino'

pattern4 = re.compile('^[a]......')

d = re.fullmatch(pattern4, string4)

print(d)  # <re.Match object; span=(0, 7), match='avelino'>

# Teste 4.1
string5 = 'a'

pattern5 = re.compile('[^b]')  

e = re.fullmatch(pattern5, string5)

print(e)  #  <re.Match object; span=(0, 1), match='a'>

# Teste 4.2
string6 = 'b'

pattern6 = re.compile('[^b]')  

f = re.fullmatch(pattern6, string6)

print(f)  # None

# Teste 5
string7 = 'b'

pattern7 = re.compile('^[\w]')  

g = re.fullmatch(pattern7, string7)

print(g)  # <re.Match object; span=(0, 1), match='b'>

# Teste 6
string8 = 'b'

pattern8 = re.compile('^[\W]')  

h = re.fullmatch(pattern8, string8)

print(h)  # None

# Teste 7
string9 = 'b'

pattern9 = re.compile('^[\s]')  

i = re.fullmatch(pattern9, string9)

print(i)  # None

# Teste 8
string10 = 'b'

pattern10 = re.compile('^[\S]')  

j = re.fullmatch(pattern10, string10)

print(j)  # <re.Match object; span=(0, 1), match='b'>

# Teste 9
string11 = '0'

pattern11 = re.compile('^[\d]')  

k = re.fullmatch(pattern11, string11)

print(k)  # <re.Match object; span=(0, 1), match='0'>

# Teste 10
string12 = '0'

pattern12 = re.compile('^[\D]')  

l = re.fullmatch(pattern12, string12)

print(l)  # None

# Teste 11
string13 = '0.21m2 '

pattern13 = re.compile('[\w\s]')  

m = re.findall(pattern13, string13)

print(m)  # ['0', '2', '1', 'm', '2', ' ']

# Teste 12
string14 = '0.21m2 '

pattern14 = re.compile('[a-z]')  

n = re.findall(pattern14, string14)

print(n)  # ['m']

# Teste 13
string15 = 'Gabriel Avelino7'

pattern15 = re.compile('[a-mA-Z0-9]')  

o = re.findall(pattern15, string15)

print(o)  # ['G', 'a', 'b', 'i', 'e', 'l', 'A', 'e', 'l', 'i', '7']

# Teste 14.1
string16 = 'Gabriel Avelino7'

pattern16 = re.compile('^[a-mA-Z0-1]')  

p = re.findall(pattern16, string16)

print(p)  # ['G']

# Teste 14.2
string17 = '5abriel Avelino7'

pattern17 = re.compile('^[a-mA-Z0-1]')  

q = re.findall(pattern17, string17)

print(q)  # []

# Teste 15 
string18 = 'GABRIELAVELINO1'

pattern18 = re.compile('[a-mA-Z0-1]+')  

r = re.fullmatch(pattern18, string18)

print(r)  # <re.Match object; span=(0, 15), match='GABRIELAVELINO1'>

# Teste 16 
string19 = ''

pattern19 = re.compile('[a-mA-Z0-1]*')  

s = re.fullmatch(pattern19, string19)

print(s)  # <re.Match object; span=(0, 0), match=''>

# Teste 17
string20 = 'GABRIELAVELINO1GABRIELAVELINO1'

pattern20 = re.compile('[a-mA-Z0-1]?')  

t = re.fullmatch(pattern20, string20)

print(t)  # None

# Teste 18
string21 = 'Caio'

pattern21 = re.compile('[a-zA-Z0-1]{4}')  

t = re.fullmatch(pattern21, string21)

print(t)  # <re.Match object; span=(0, 4), match='Caio'>

# Teste 18
string21 = 'Gabriel'

pattern21 = re.compile('[a-zA-Z0-1]{4,8}')  

t = re.fullmatch(pattern21, string21)

print(t)  # <re.Match object; span=(0, 7), match='Gabriel'>
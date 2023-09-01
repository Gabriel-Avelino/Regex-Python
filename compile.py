import re

string1 = 'Gabriel'
string2 = 'Gabriel Gabriel'

# compile: Cria um padrão de string.
pattern = re.compile('Gabriel')

# fullmatch(): Verifica se a string inteira atende ao padrão definido no compile.
x = re.fullmatch(pattern, string1)
y = re.fullmatch(pattern, string2)

print(x)  # <re.Match object; span=(0, 7), match='Gabriel'>
print(y)  # None
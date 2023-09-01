import re

string1 = 'Olá Gabriel'

pattern = re.compile('Gabriel')

# search: Verifica toda a string para saber se partes dela seguem esse padrão. Busca apenas a primeira vez que o padrão é atendido.
x = re.search(pattern, string1)

print(x)  # <re.Match object; span=(4, 11), match='Gabriel'>

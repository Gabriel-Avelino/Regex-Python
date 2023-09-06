import re 

string = 'gabriel.avelino7@gmail.com'
pattern = re.compile('[\.\w]+@[\w]+\.[a-zA-Z]{2,3}[\.a-zA-Z]{0,3}')
x = re.fullmatch(pattern, string)
print(x)
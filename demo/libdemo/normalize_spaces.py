
import re

with open('test.txt', 'rt') as f:
    contents = f.read()

result = re.sub(' +', ' ', contents)

#print(result)

with open('test2.txt', 'wt') as f:
    f.write(result)





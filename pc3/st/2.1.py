"""
Splitting Strings on Any of Multiple Delimiters
"""
import re

line = 'asd fjdk; afed, fjek,asdf,           foo'
print(re.split(r'[;,\s]\s*', line))  # , : space as separator or white space followed by any amout of wss
fields = re.split(r'(;|,|\s)\s*', line)  # () include match pattern
print(fields)
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
print(''.join(v + d for v, d in zip(values, delimiters)))
print(re.split(r'(?:,|;|\s)\s*', line))
print()

"""
Matching Text at the Start or End of a String
"""
import os
import re
from urllib.request import urlopen

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))
print()

filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith('.py')])
print(any(name.endswith('.py') for name in filenames))
print()


def read_date(nm):
    if nm.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(nm).read()
    else:
        with open(nm) as f:
            return f.read()


choices = ['http:', 'ftp:']
url = 'http://www.python.org'
# print(url.startswith(choices)) startswith || endswith need tuple()
print(url.startswith(tuple(choices)))
print(read_date(url))
print()

print(filename[-4:] == '.txt')
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')
print()

print(re.match('http:|https|ftp:', url))  # overkill for simple matching

# if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
#     ...

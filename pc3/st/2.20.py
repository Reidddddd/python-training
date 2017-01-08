"""
Performing Text Operations on Byte Strings
"""
import re

data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))
print()

data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

data = b'FOO:BAR:SPAM'
# print(re.split('[:,]', data))
print(re.split(b'[:,]', data))
print()

a = 'Hello World'
print(a[0])
print(a[1])
b = b'Hello World'
print(b[0])
print(b[1])

print()
s = b'Hello World'
print(s)
print(s.decode('ascii'))

# no string formatting operations available to byte strings
# b'%10s %10d %10.2f' % (b'ACME', 100, 490.1)
# B'{} {} {}'.format(b'ACME', 100, 490.1)
print()
print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))
print()

with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')
import os

print(os.listdir('.'))
print(os.listdir(b'.'))

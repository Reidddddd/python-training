"""
Working with Binary, Octal, and Hexadecimal Integers
"""
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

# output include signed
x = -1234
print(format(x, 'b'))
print(format(x, 'x'))
# unsigned value
print(format(2**32 + x, 'b'))
print(format(2**32 + x, 'x'))
# convert integer strings in different bases
print(int('4d2', 16))
print(int('10011010010', 2))

import os

os.chmod("D:\development\workspace\python-training\whatsnew.txt", 0o755)

b'still allows embedded "double" quotes'
b"still allows embedded 'single' quotes"
b"""3 single quotes""", b"""3 double quotes"""

# created
bytes(10)
bytes(range(20))

print(bytes.fromhex('2ef0 f1f2'))

# bytearray mutable
bytearray()
bytearray(10)
bytearray(b'Hi!')

print(bytearray.fromhex('2ef0f1f2'))

# Bytes and Bytearray Operations
a = "abc"
b = a.replace("a", "f")
print(a, b)
a = b"abc"
b = a.replace(b"a", b"f")
print(a, b)

bo = b'Py' in b'Python'
print(bo)

sb = b'1,2,3'.split(b',')
print(sb)
sb = b'1,2,3'.split(b',', maxsplit=1)
print(sb)
sb = b'1,2,,3,'.split(b',')
print(sb)
sb = b'1 2 3'.split()
print(sb)
sb = b'1 2 3'.split(maxsplit=1)
print(sb)
sb = b'   1  2   3   '.split()
print(sb)

stri = b'      spacious   '.strip()
print(stri)
stri = b'www.example.com'.strip(b'cmowz.')
print(stri)

et = b'01\t012\t0123\t01234'.expandtabs()
print(et)
et = b'01\t012\t0123\t01234'.expandtabs(4)
print(et)

print(b'ABCabc1'.isalnum())
print(b'ABC abc1'.isalnum())
print(b'1234'.isdigit())
print(b'1.23'.isdigit())
print(b'hello world'.islower())
print(b'Hello world'.islower())
print(b'Hello World'.istitle())
print(b'Hello world'.istitle())
print(b'HELLO WORLD'.isupper())
print(b'Hello world'.isupper())
print(b'Hello World'.lower())

spl = b'ab c\n\nde fg\rkl\r\n'.splitlines()
print(spl)
spl = b'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
print(spl)

print(b'Hello World'.swapcase())
print(b'hello world'.title())

print(b"they're bill's friends from the UK".title())
import re


def titlecase(s):
    return re.sub(rb"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0)[0:1].upper() +
                             mo.group(0)[1:].lower(), s)
print(titlecase(b"they're bill's friends from the UK"))

print(b'Hello World'.upper())

print(b"42".zfill(5))
print(b"-42".zfill(5))

# Memory Views
# allow python code to access the internal data of an object that
# supports the buffer protocol without copying
print("\n********** Memory Views ***********")
v = memoryview(b'abcefg')
print(v[1])
print(v[-1])
print(v[1:4])
print(bytes(v[1:4]))

import array

a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
print(a[0])
print(a[-1])
print(a[2:3].tolist())
print(a[::2].tolist())
print(a[::-1].tolist())
print()

data = bytearray(b'abcefg')
v = memoryview(data)
print(v.readonly)
v[0] = ord(b'z')
print(data)
v[1:4] = b'123'
print(data)
# v[2:3] = b'spam'
v[2:6] = b'spam'
print(data)

print("!!!!!!!!!!!!!")
v = memoryview(b'abcefg')

print(hash(v) == hash(b'abcefg'))
print(hash(v[2:4]) == hash(b'ce'))
print(hash(v[::-2]) == hash(b'abcefg'[::-2]))

import array

print("\n__eq__")
a = array.array('I', [1, 2, 3, 4, 5])
b = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
c = array.array('b', [5, 3, 1])
x = memoryview(a)
y = memoryview(b)
print(x == a == y == b)
print(x.tolist() == a.tolist() == y.tolist() == b.tolist())
z = y[::-2]
print(z == c)
print(z.tolist() == c.tolist())

from ctypes import BigEndianStructure, c_long
class BEPoint(BigEndianStructure):
    _fields_ = [("x", c_long), ("y", c_long)]

point = BEPoint(100, 200)
a = memoryview(point)
b = memoryview(point)
print(a == point)
print(b == point)
print(a == b)

# tobytes()
print('\n*****tobytes()*****')
m = memoryview(b"abc")
print(m.tobytes())
print(bytes(m))

# tolist()
print('\n*****tolist()*****')
print(memoryview(b"abc").tolist())
import array

a = array.array('d', [1.1, 2.2, 3.3])
m = memoryview(a)
print(m.tolist())

# release()
print('\n*****release()*****')
m = memoryview(b'abc')
m.release()
# m[0]
# forbidden on released memoryview object
with memoryview(b'abc') as m:
    print(m[0])
# m[0]
# forbidden on released memoryview object

# cast()
print('\n*****cast()*****')
import array
a = array.array('l', [1,2,3])
x = memoryview(a)
print(x.format)
print(x.itemsize)
print(len(x))
print(x.nbytes)

y = x.cast('B')
print(y.format)
print(y.itemsize)
print(len(y))
print(y.nbytes)

b = bytearray(b'zyz')
x = memoryview(b)
# x[0] = b'a' invalid value for format "B"
y = x.cast('c')
y[0] = b'a'
print(b)

import struct

buf = struct.pack("i" * 12, *list(range(12)))
x = memoryview(buf)
y = x.cast('i', shape=[2,2,3])
print(y.tolist())
print(y.format)
print(y.itemsize)
print(len(y))
print(y.nbytes)
z = y.cast('b')
print(z.format)
print(z.itemsize)
print(len(z))
print(z.nbytes)

buf = struct.pack("L"*6, *list(range(6)))
x = memoryview(buf)
y = x.cast('L', shape=[2,3])
print(len(y))
print(y.nbytes)
print(y.tolist())

# obj
print("\n*******obj*********")
b = bytearray(b'xyz')
m = memoryview(b)
print(m.obj is b)

# nbytes
print("\n*******nbytes*********")
import array

a = array.array('i', [1,2,3,4,5])
m = memoryview(a)
print(len(m))
print(m.nbytes)
y = m[::2]
print(len(y))
print(y.nbytes)
print(len(y.tobytes()))

# itemsize
print("\n*****itemsize*****")
import array, struct

m = memoryview(array.array('H', [32000, 32001, 32002]))
print(m.itemsize)
print(m[0])
print(struct.calcsize('H') == m.itemsize)

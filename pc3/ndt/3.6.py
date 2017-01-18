"""
Performing Complex-Valued Math
"""
a = complex(2, 4)
b = 3 -5j
print(a)
print(b)
print(a.real)
print(a.imag)
print(a.conjugate())
c = a + b
d = a * b
e = a / b
print(c)
print(d)
print(e)
print(abs(a))

import cmath

print()
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

import numpy as np

print()
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a + 2)
print(np.sin(a))

# import math
# do not produce complex values
# math.sqrt(-1)

import cmath

print()
print(cmath.sqrt(-1))

"""
Working with Infinity and NaNs
"""
import math

a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(b)
print(c)
print(math.isinf(a))
print(math.isnan(c))

# Infinite value will be propagated in calculations
a += 45
print(a)
a *= 100
print(a)
d = 10 / a
print(d)

# Certain operations are undefined and will result in a NaN
e = a / a
print(e)
print(a + b)

# NaN values propagate through all operations without raising an exception
c += 23
c /= 2
c *= 2
c = math.sqrt(c)
print(c)

# NaN value never compare as equale
c = float('nan')
d = float('nan')
print(c == d)
print(c is d)

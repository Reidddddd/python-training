"""
Unpacking a Sequence into Separate Variables
"""
p = (4, 5)
x, y = p
print(x)
print(y)
print()

data = ['acme', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(date)
name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(day)
print()

# Unpacking works with any object that happens to be iterable.
s = 'Momo'
a, b, c, d = s
print(a)
print(b)
print(d)
print()

# Throw away some variables
_, shares, price, _ = data
print(shares)
print(price)

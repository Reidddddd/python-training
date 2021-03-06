"""
Calculating with Large Numerical Arrays
"""
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x * 2)
# print(x + 10) error
print(x + y)

import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)


def f(x):
    return 3*x**2 - 2*x + 7

print(f(ax))

print(np.sqrt(ax))
print(np.cos(ax))

# Two-dimensional grid
# grid = np.zeros(shape=(10000,10000), dtype=float)
# print(grid)
# grid += 10
# print(grid)
# grid = np.sin(grid)
# print(np.sin(grid))

# Indexing functionality
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[1]) # row 1
print(a[:,1]) # column 1
# Select a subregion and change it
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a)

# Broadcast a row vector across an operation on all rows
b = a + [100, 101, 102, 103]
print(b)

# Conditional assignment on an array
print(np.where(a < 10, a, 10))

"""
Deque is a double-ended queue. It supports thread-safe, memory efficient appends and pops
from either side of the deque with approximately the same O(1) performance in either direction
"""
from collections import deque

import itertools

d = deque('ghi')
for elem in d:
    print(elem.upper())
print()

d.append('j')
d.appendleft('f')
print(d)
print()

print(d.pop())
print(d.popleft())
print(list(d))
print(d[0])
print(d[-1])
print()

print(list(reversed(d)))
print(('h' in d))
d.extend('jkl')
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)
print()

dd = deque(reversed(d))
d.clear()
d.extendleft('abc')
print(d)
print()


def tail(filename, n=10):
    'Return the last n lines of a file'
    with open(filename) as f:
        return deque(f, n)


print(tail("Counter.py"))
print()


def moving_average(iterable, n=3):
    # moving_average([40,30,50,46,39,44])
    it = iter(iterable)
    d = deque(itertools.islice(it, n - 1))
    print(d)
    d.appendleft(0)
    s = sum(d)
    for e in it:
        s += e - d.popleft()
        d.append(e)
        yield s / n


ma = moving_average([40, 30, 50, 46, 39, 44])
for i in ma:
    print(i)

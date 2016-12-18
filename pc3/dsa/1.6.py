"""
Mapping Keys to Multiple Values in a Dictionary
"""
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['b'].append(5)
d['c'].append('!')
d['c'].append('?')
print(d)
print()

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(2)
d['a'].add(1)
d['b'].add(4)
d['b'].add(4)
d['b'].add(5)
d['b'].add(5)
d['c'].add('!')
d['c'].add('!')
d['c'].add('?')
d['c'].add('?')
print(d)
print()

pairs = [
    ('a', 1),
    ('b', 2),
    ('c', 3),
    ('d', 4),
    ('e', 5),
    ('a', 6)
]
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print(d)

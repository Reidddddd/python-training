"""
key: value pairs.
defalutdict([default_factory[, ...]])
"""
from collections import defaultdict

s = [
    ('yellow', 1),
    ('blue', 2),
    ('yellow', 3),
    ('blue', 4),
    ('red', 1)
]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(list(d.items()))
print()

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(list(d.items()))
print()


def constant_factory(value):
    return lambda: value


d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
print('%(name)s %(action)s to %(object)s' % d)
print()

s = [
    ('red', 1),
    ('blue', 2),
    ('red', 3),
    ('blue', 4),
    ('red', 1),
    ('blue', 4),
]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)
print(list(d.items()))


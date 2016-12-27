"""
Combining and Concatenating Strings
"""
parts = ['Is', 'Chicago', 'Not', 'Chicago']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

a = 'Is Chicago'
b = 'Not Chicago'
print(a + ' ' + b)

print('{} {}'.format(a, b))

print()
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

c = '!'
print(a, b, c, sep=':')


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago'


text = '**'.join(sample())
print(text)


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

"""
Unpacking Elements from Iterables of Arbitrary Length
"""
from statistics import mean


def drop_first_last(grades):
    first, *middle, last = grades
    return mean(middle)

grads = (1, 2, 3, 4, 5, 6, 7, 8)
print(drop_first_last(grads))
print()

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numers = record
print(name)
print(email)
print(phone_numers)
print()

*trailing, current = grads
print(trailing)
print(current)
print()

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
print()

# combined with certain kinds of string processing
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
print(fields)
print()

rec = ('acme', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = rec
print(name)
print(year)
print()

items = [1, 10, 7, 4, 5, 9]
head, *tails = items
print(head)
print(tails)
print()


def summary(its):
    hd, *tail = its
    return hd + sum(tail) if tail else hd

print(summary(items))

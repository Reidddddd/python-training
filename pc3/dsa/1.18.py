"""
Mapping Names to Sequence Elements
"""
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
print(len(sub))
addr, joined = sub
print(addr)
print(joined)

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


s = Stock('acme', 100, 123.45)
print(s)
# s.shares = 75 immutable
s = s._replace(shares=75)
print(s)
print()

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'acme', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))

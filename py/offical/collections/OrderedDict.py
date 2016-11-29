"""
It remembers the order that items were inserted.
"""
from collections import OrderedDict, Counter

d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
print(''.join(d.keys()))
d.move_to_end('b', last=False)
print(''.join(d.keys()))
print()

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
o = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
print(o)
o = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
print(o)
o = OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
print(o)


class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)


class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

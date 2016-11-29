"""
A ChainMap class is provided for quickly linking a number of mappings
so they can be treated as a single unit.
"""
from collections import ChainMap
import builtins
import os
import argparse

pylookup = ChainMap(locals(), globals(), vars(builtins))
print(pylookup)
print()

defaults = {
    'color': 'red',
    'user': 'guest'
}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}
combined = ChainMap(command_line_args, os.environ, defaults)
print(combined['color'])
print(combined['user'])
print()

c = ChainMap()
d = c.new_child()
e = c.new_child()
print(e.maps[0])
print(e.maps[-1])
print(e.parents)
print()

d['x'] = 1
print(d['x'])
print(list(d))
for k in d:
    print(k)
print(len(d))
print(d.items())
print(dict(d))
del d['x']
print()


class DeepChainMap(ChainMap):
    'Variant of ChainMap that allows direct updates to inner scopes'

    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)


d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
d['lion'] = 'orange'
d['snake'] = 'red'
del d['elephant']
print(d)

d = ChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
d['lion'] = 'green'
d['elephant'] = 'white'
d['zebra'] = 'purple'
print(len(d))
del d['lion']
print(d)

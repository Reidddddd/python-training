"""
A counter tool is provided to support convenient and rapid tallies
"""
import re
from collections import Counter

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)
print()

words = re.findall \
    (r'\w+', open('D:\development\workspace\python-training\whatsnew.txt').read().lower())
print(Counter(words).most_common(10))
print()

c = Counter('gallahad')
print(c)
c = Counter({'red': 4, 'blue': 2})
print(c)
c = Counter(cats=4, dogs=8)
print(c)
del c['cats']
print(c)
print()

c = Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))
print(Counter('abracadabra').most_common(3))
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)
print()

c = Counter(a=4, b=2, c=0, d=-2)
print(sum(c.values()))
print(list(c))
print(set(c))
print(dict(c))
print(c.items())
print(+c)
print(Counter(words).most_common()[:(-10 - 1):-1])
print(c.clear())
pairs = [('a', 1), ('b', 2), ('c', 3)]
print(Counter(dict(pairs)))
print()

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print(c + d)
print(c - d)
print(c & d)
print(c | d)
print()

c = Counter(a=2, b=-1)
print(+c)
print(-c)
print()

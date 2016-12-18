"""
Transforming and Reducing Data ath the Same Time
"""
from os import listdir

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

files = listdir('D:\development\workspace\python-training\pc3\ch1\dsa')
if any(name.endswith('.py') for name in files):
    print('There be python')
else:
    print('Sorry, no python')
print()

s = ('acme', 50, 123.45)
print('.'.join(str(x) for x in s))
print()

portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)
print()

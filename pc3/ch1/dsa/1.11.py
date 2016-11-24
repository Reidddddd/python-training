"""
Naming a Slice
"""
record = '....................100          .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])
print(cost)

shares = slice(20, 32)
price = slice(40, 48)
cost = int(record[shares]) * float(record[price])
print(cost)
print()

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)
print()

a = slice(1, 50, 2)
print(a.start)
print(a.stop)
print(a.step)
print()

s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])
print()

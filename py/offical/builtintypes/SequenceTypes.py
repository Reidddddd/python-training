print('gg' in 'eggs')

lists = [[]] * 3
print(lists)
lists[0].append(3)  # not copied, instead, they are referenced multiple times
print(lists)
lists = [[] for i in range(3)]
lists[0].append(3)
lists[1].append(5)
lists[2].append(7)
print(lists)
print()

print(list(range(10)))
print(list(range(1, 11)))
print(list(range(0, 30, 5)))
print(list(range(0, 10, 3)))
print(list(range(0, -10, -1)))
print(list(range(0)))
print(list(range(1, 0)))
r = range(0, 20, 2)
print(r)
print(11 in r)
print(10 in r)
print(r.index(10))
print(r[5])
print(r[:5])
print(r[-1])


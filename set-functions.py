import pickle

a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 4, 5, 6, 7}
a.add(8)
print(a)

a.update([10, 11])
print(a)

a.discard(10)
print(a)

a.intersection(b)
a.difference(b)
a.union(b)
b = frozenset(a)

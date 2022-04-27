# Lists
l = [1,'ART',3]

# Adding Element into list
l.append(14)
l.append(23)
print("Adding 14 and 23 in list", l)

# Popping Elements from list
l.pop()
print("Popped one element from list", l)
print()

# Array
a = [1,4,6]

# Adding Element into array
a.append(14)
a.append(23)
print("Adding 14 and 23 in array", a)
# Tuple
t = tuple(a)

# Tuples are immutable
print("\nTuple", t)
print()

# Dictionary
d = {}

# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)

# Removing key-value pair
del d[10]
print("Dictionary", d)

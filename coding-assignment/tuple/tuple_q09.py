#Find the union, intersection, and difference of two tuples:
t1 = (1, 2, 3)
t2 = (3, 4, 5)

union = tuple(set(t1).union(t2))
intersection = tuple(set(t1).intersection(t2))
difference = tuple(set(t1).difference(t2))

print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)

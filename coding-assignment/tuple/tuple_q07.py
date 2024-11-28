#7 Check if all elements in a tuple are the same:
t = (1, 1, 1, 1)
all_same = all(x == t[0] for x in t)
print(all_same)

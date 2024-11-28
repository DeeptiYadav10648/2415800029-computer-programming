#Interchange the first and last elements in a tuple:
t = (1, 2, 3, 4, 5)
if len(t) > 1:
    t = (t[-1],) + t[1:-1] + (t[0],)
print("Interchanged tuple:", t)

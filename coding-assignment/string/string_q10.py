#10 Check if Two Strings are Rotations of Each Other
st = input()
a = st.split()
b = a[0]
c = a[1]
if len(b)==len(c) and c in (b+b):
    print(True)
else:
    print(False)

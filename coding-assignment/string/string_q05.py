#5 Check if Two Strings are Anagrams
st=input()
one=st.split(' ')
a=one[0]
b=one[1]
c=sorted(a)
d=sorted(b)
if c==d:
    print(True)
else:
    print(False)

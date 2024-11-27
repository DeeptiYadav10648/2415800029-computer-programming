#8 Count frequency of each character in alphabetical order
st=input()
out=sorted(st)
fre=""
for char in out:
    if char not in fre:
        print(f'{char}:{st.count(char)}')
    fre=fre+char

#12 Compress a String Using the Counts of Repeated Characters
st = input()
fre=""
for char in st:
    if char not in fre:
        a=st.count(char)
        fre=fre+char
        print(f'{char}{a}',end="")

#9 Find the first Non-repeating Character
st=input()
nonrep=""
for char in st:
    a=st.count(char)
    if a==1:
        print(char)
        break

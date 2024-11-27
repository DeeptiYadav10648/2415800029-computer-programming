#6 Find the longest word in a string
st=input()
st1=st.split(' ')
for char in st1:
    if len(char)>len(st1):
        print(char)

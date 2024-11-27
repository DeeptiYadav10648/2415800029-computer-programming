#19 The encrypted message
st=input("Encryppted message:")
Shift=int(input())
for char in st:
    a=ord(char)
    b=a-Shift
    c=chr(b)
    print(c,end='')

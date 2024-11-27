#15  Find the Longest Palindromic Substring
st = input()
fre=""
for char in st:
    a=char[::-1]
    if a==char:
        print(a)

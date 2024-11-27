#14 check if a string contains only digits
st = input()
a=True
for char in st:
 if char<'0' or char>'9':
    a=False
    print(False)
if a ==True:
    print(True)

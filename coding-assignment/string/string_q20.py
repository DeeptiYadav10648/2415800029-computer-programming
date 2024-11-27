#20 The shopping list merger
list_1=str(input("List 1:"))   
list_2=str(input("List 2:"))  
out_1=list_1.split()
out_2=list_2.split()
fre=''
for char in out_1:
    if char not in fre:
        print(char,end=' ')
        fre+= char
for char in out_2:
    if char not in fre:
        print(char,end=' ')
        fre+= char
